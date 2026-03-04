from pathlib import Path
from model_manager.domain.services.dataset_augmentor import (
    DatasetAugmentor,
    AugmentorConfig,
    AugmentorCallbacks,
    AugmentorResults
)
from pytest_mock import MockerFixture


def test_dataset_augmentor_happy_path(mocker :MockerFixture):
    # ---------------------------
    # Mocks
    # ---------------------------
    reader = mocker.Mock()
    writer = mocker.Mock()
    transform = mocker.Mock()

    # Fake Dataset: 2 Bilder
    fake_img1 = "img1"
    fake_img2 = "img2"
    fake_path1 = Path("img1.jpg")
    fake_path2 = Path("img2.jpg")

    reader.count_images.return_value = 2
    reader.iter_files.return_value = [
        (fake_img1, fake_path1),
        (fake_img2, fake_path2),
    ]
    reader.load_label_from_img.return_value = ([], [])

    # Fake Augmentation Ergebnis
    transform.return_value = {
        "image": "aug_img",
        "bboxes": [],
        "class_labels": []
    }

    # Callbacks
    on_progress = mocker.Mock()
    on_done = mocker.Mock()
    on_error = mocker.Mock()

    callbacks = AugmentorCallbacks(
        on_progress=on_progress,
        on_done=on_done,
        on_error=on_error,
    )

    # Config: 3 Augmentierungen pro Bild
    cfg = AugmentorConfig(num_augments=3)

    augmentor = DatasetAugmentor(
        config=cfg,
        transform=transform,
        reader=reader,
        writer=writer,
        callbacks=callbacks,
    )

    # ---------------------------
    # Act
    # ---------------------------
    augmentor.augment()

    # ---------------------------
    # Assert – Writer
    # ---------------------------
    # 2 Bilder * 3 Augmentierungen = 6 Saves
    assert writer.save_image.call_count == 6
    assert writer.save_label.call_count == 6

    # ---------------------------
    # Assert – Transform
    # ---------------------------
    assert transform.call_count == 6

    # ---------------------------
    # Assert – Callbacks
    # ---------------------------
    assert on_progress.call_count == 2  # pro Originalbild
    on_error.assert_not_called()
    on_done.assert_called_once()

    # Ergebnis prüfen
    result: AugmentorResults = on_done.call_args[0][0]
    assert result.total_imgs == 2
    assert result.total_aug_imgs == 6
    assert result.success == 6
    assert result.error == 0

def test_dataset_augmentor_error_path(mocker :MockerFixture):
    # ---------------------------
    # Mocks
    # ---------------------------
    reader = mocker.Mock()
    writer = mocker.Mock()
    transform = mocker.Mock()

    fake_img = "img1"
    fake_img2 = "img1"
    fake_path = Path("img1.jpg")
    fake_path2 = Path("img1.jpg")

    reader.count_images.return_value = 2
    reader.iter_files.return_value = [(fake_img, fake_path), (fake_img2, fake_path2)]
    reader.load_label_from_img.return_value = ([], [])

    # Erste Augmentation ok, zweite wirft Fehler
    transform.side_effect = [
        {
            "image": "aug_img",
            "bboxes": [],
            "class_labels": []
        },
        Exception("augmentation failed"),
        {
            "image": "aug_img",
            "bboxes": [],
            "class_labels": []
        },
        {
            "image": "aug_img2",
            "bboxes": [],
            "class_labels": []
        },
        Exception("augmentation failed"),
        {
            "image": "aug_img2",
            "bboxes": [],
            "class_labels": []
        },
    ]

    on_progress = mocker.Mock()
    on_done = mocker.Mock()
    on_error = mocker.Mock()

    callbacks = AugmentorCallbacks(
        on_progress=on_progress,
        on_done=on_done,
        on_error=on_error,
    )

    cfg = AugmentorConfig(num_augments=3)

    augmentor = DatasetAugmentor(
        config=cfg,
        transform=transform,
        reader=reader,
        writer=writer,
        callbacks=callbacks,
    )

    # ---------------------------
    # Act
    # ---------------------------
    augmentor.augment()

    # ---------------------------
    # Assert – Transform
    # ---------------------------
    assert transform.call_count == 6  

    # ---------------------------
    # Assert – Writer
    # ---------------------------
    assert writer.save_image.call_count == 4
    assert writer.save_label.call_count == 4

    # ---------------------------
    # Assert – Callbacks
    # ---------------------------
    assert on_error.call_count == 2
    assert on_progress.call_count == 2
    on_done.assert_called_once()

    # ---------------------------
    # Assert – Results
    # ---------------------------
    result: AugmentorResults = on_done.call_args[0][0]

    assert result.total_imgs == 2
    assert result.total_aug_imgs == 6
    assert result.success == 4
    assert result.error == 2