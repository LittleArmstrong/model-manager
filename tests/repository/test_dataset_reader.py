import pytest
from pathlib import Path
import numpy as np
import cv2
import yaml

from model_manager.repository.dataset_reader import DatasetReader, RawDatasetReader
from model_manager.repository.dataset_loader import YoloDatasetLoader, YoloDataset, RawDataset

# --- Fixtures ---

@pytest.fixture
def fake_dataset1():
    root = Path("tests/data").resolve()
    dataset_dir = root / "yolo_dataset1"
    return YoloDatasetLoader.load(dataset_dir)

# --- Tests ---

# -- DatasetReader
def test_iter_files_images(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    files = list(reader.iter_files("train", "images", load=False))
    assert len(files) == 2
    names = {p.name for p in files}
    assert names == {"img_0.png", "img_1.jpg"}

def test_iter_files_labels(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    labels = list(reader.iter_files("train", "labels", load=True))

    assert len(labels) == 2
    all_boxes = []
    all_classes = []
    all_paths = []

    for boxes, classes, path in labels:
        all_boxes.extend(boxes)
        all_classes.extend(classes)
        all_paths.append(path)

    assert [0.5, 0.5, 0.2, 0.2] in all_boxes
    assert [0.4, 0.4, 0.2, 0.2] in all_boxes
    assert [0.3, 0.3, 0.1, 0.1] in all_boxes
    assert set(all_classes) == {0, 1, 2}
    names = {p.name for p in all_paths}
    assert names == {"img_1.txt", "img_0.txt"}

def test_count_images(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    assert reader.count_images("train") == 2
    assert reader.count_images("val") == 2
    assert reader.count_images("test") == 2

def test_load_images(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    images = list(reader.iter_files("test", "images", load=True))
    all_imgs = []
    all_paths = []
    for img, path in images:
        all_imgs.append(img)
        all_paths.append(path)
    names = {p.name for p in all_paths}
    assert names == {"img_1.jpg", "img_0.png"}
    assert all(img.shape == (10, 10, 3) for img in all_imgs)

def test_load_image(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    img_path = fake_dataset1.train_images / "img_1.jpg"
    img = reader.load_image(img_path)
    assert img.shape == (10, 10, 3)

def test_load_info(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    meta = reader.load_info()
    assert meta["names"] == ["cat", "dog"]
    assert meta["nc"] == 2
    assert meta["train"] == "images/train"
    assert meta["val"] == "images/val"
    assert meta["test"] == "images/test"

def test_lbl_from_img(fake_dataset1):
    reader = DatasetReader(fake_dataset1)
    img_path = Path("tests/data/yolo_dataset1/images/train/img_0.png").resolve()
    label_path = Path("tests/data/yolo_dataset1/labels/train/img_0.txt").resolve()
    assert label_path.exists()
    bboxes, classes = reader.load_label_from_img(img_path)
    assert bboxes == [[0.5, 0.5, 0.2, 0.2]]
    assert classes == [0]

# -- RawDatasetReader

def test_iter_image_label_pairs(tmp_path:Path):
    images = tmp_path / "images"
    labels = tmp_path / "labels"
    images.mkdir(parents=True, exist_ok=True)
    labels.mkdir(parents=True, exist_ok=True)

    img1 = images / "a.png"
    img2 = images / "b.png"

    lbl1 = labels / "a.txt"
    lbl2 = labels / "b.txt"

    img1.touch()
    img2.touch()
    lbl1.touch()
    lbl2.touch()

    ds = RawDataset(tmp_path, (images,), (labels,))

    ds_reader = RawDatasetReader(ds)
    pairs = list(ds_reader.iter_pairs())

    assert set(pairs) == {(img1, lbl1), (img2, lbl2)}

def test_iter_image_label_pairs_multiple_image_folders(tmp_path:Path):
    images = tmp_path / "images"
    images2 = tmp_path / "img"
    labels = tmp_path / "labels"
    images.mkdir(parents=True, exist_ok=True)
    images2.mkdir(parents=True, exist_ok=True)
    labels.mkdir(parents=True, exist_ok=True)


    img1 = images / "a.png"
    img2 = images2 / "b.png"
    lbl1 = labels / "a.txt"
    lbl2 = labels / "b.txt"

    img1.touch()
    img2.touch()
    lbl1.touch()
    lbl2.touch()

    ds = RawDataset(tmp_path, (images, images2), (labels,))

    ds_reader = RawDatasetReader(ds)
    pairs = list(ds_reader.iter_pairs())

    assert set(pairs) == {(img1, lbl1), (img2, lbl2)}

def test_iter_image_label_pairs_multiple_folders(tmp_path:Path):
    images = tmp_path / "images"
    images2 = tmp_path / "img"
    labels = tmp_path / "labels"
    labels2 = tmp_path / "lbls"
    images.mkdir(parents=True, exist_ok=True)
    images2.mkdir(parents=True, exist_ok=True)
    labels.mkdir(parents=True, exist_ok=True)
    labels2.mkdir(parents=True, exist_ok=True)

    img1 = images / "a.png"
    img2 = images2 / "b.png"
    lbl1 = labels / "a.txt"
    lbl2 = labels2 / "b.txt"

    img1.touch()
    img2.touch()
    lbl1.touch()
    lbl2.touch()

    ds = RawDataset(tmp_path, (images, images2), (labels, labels2))

    ds_reader = RawDatasetReader(ds)
    pairs = list(ds_reader.iter_pairs())

    assert set(pairs) == {(img1, lbl1), (img2, lbl2)}

def test_iter_image_label_pairs_eception_same_files(tmp_path:Path):
    images = tmp_path / "images"
    images2 = tmp_path / "img"
    labels = tmp_path / "labels"
    labels2 = tmp_path / "lbls"
    images.mkdir(parents=True, exist_ok=True)
    images2.mkdir(parents=True, exist_ok=True)
    labels.mkdir(parents=True, exist_ok=True)
    labels2.mkdir(parents=True, exist_ok=True)

    img1 = images / "a.png"
    img2 = images2 / "a.png"
    lbl1 = labels / "a.txt"
    lbl2 = labels2 / "a.txt"

    img1.touch()
    img2.touch()
    lbl1.touch()
    lbl2.touch()

    ds = RawDataset(tmp_path, (images, images2), (labels, labels2))

    ds_reader = RawDatasetReader(ds)
    with pytest.raises(ValueError):
        list(ds_reader.iter_pairs())

def test_iter_image_label_pairs_same_files_different_depth(tmp_path:Path):
    images = tmp_path / "images"
    images2 = tmp_path / "img" / "a"
    labels = tmp_path / "labels"
    labels2 = tmp_path / "lbls" / "a"
    images.mkdir(parents=True, exist_ok=True)
    images2.mkdir(parents=True, exist_ok=True)
    labels.mkdir(parents=True, exist_ok=True)
    labels2.mkdir(parents=True, exist_ok=True)

    img1 = images / "a.png"
    img2 = images2 / "a.png"
    lbl1 = labels / "a.txt"
    lbl2 = labels2 / "a.txt"

    img1.touch()
    img2.touch()
    lbl1.touch()
    lbl2.touch()

    ds = RawDataset(tmp_path, (images, images2), (labels, labels2))

    ds_reader = RawDatasetReader(ds)
    pairs = list(ds_reader.iter_pairs())

    assert set(pairs) == {(img1, lbl1), (img2, lbl2)}

def test_iter_image_label_pairs_direct_label_priority(tmp_path: Path):
    images = tmp_path / "images"
    labels = tmp_path / "labels"
    images.mkdir()
    labels.mkdir()

    img = images / "a.png"
    direct_lbl = images / "a.txt"
    other_lbl = labels / "a.txt"

    img.touch()
    direct_lbl.touch()
    other_lbl.touch()

    ds = RawDataset(tmp_path, (images,), (labels,))
    pairs = list(RawDatasetReader(ds).iter_pairs())

    assert pairs == [(img, direct_lbl)]


def test_iter_image_label_pairs_image_without_label(tmp_path: Path):
    images = tmp_path / "images"
    labels = tmp_path / "labels"
    images.mkdir()
    labels.mkdir()

    img = images / "a.png"
    random_lbl = labels / "b.txt"
    img.touch()
    random_lbl.touch()

    ds = RawDataset(tmp_path, (images,), (labels,))
    pairs = list(RawDatasetReader(ds).iter_pairs())

    assert pairs == [(img, None)]

def test_iter_image_label_pairs_choose_closest_label(tmp_path: Path):
    images = tmp_path / "a" / "images"
    labels1 = tmp_path / "a" / "labels"
    labels2 = tmp_path / "labels"

    images.mkdir(parents=True)
    labels1.mkdir(parents=True)
    labels2.mkdir(parents=True)

    img = images / "x.png"
    lbl_close = labels1 / "x.txt"
    lbl_far = labels2 / "x.txt"

    img.touch()
    lbl_close.touch()
    lbl_far.touch()

    ds = RawDataset(tmp_path, (images,), (labels1, labels2))
    pairs = list(RawDatasetReader(ds).iter_pairs())

    assert pairs == [(img, lbl_close)]

