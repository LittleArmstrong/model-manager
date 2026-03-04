import pytest
from pathlib import Path

from model_manager.domain.services.dataset_validator import YoloDatasetValidator
from model_manager.domain.models.dataset import YoloDataset
from model_manager.repository.dataset_loader import YoloDatasetLoader

# --- Fixtures ---

@pytest.fixture
def fake_dataset1():
    # Dummy Dataset Struktur
    root = Path("tests/data").resolve()
    dataset_dir = root / "yolo_dataset1"
    return YoloDatasetLoader.load(dataset_dir)


@pytest.fixture
def invalid_dataset_no_train_labels_path(fake_dataset1):
    
    return YoloDataset(
        root=fake_dataset1.root,
        train_images=fake_dataset1.train_images,
        train_labels=None,  # ❌ invalid
        val_images=fake_dataset1.val_images,
        val_labels=fake_dataset1.val_labels,
        test_images=fake_dataset1.test_images,
        test_labels=fake_dataset1.test_labels,
        yaml_path=fake_dataset1.yaml_path,
        num_classes=2,
        class_names=("cat", "dog"),
    )

@pytest.fixture
def invalid_dataset_empty_train_labels():
    root = Path("tests/data").resolve()
    dataset_dir = root / "yolo_invalid_dataset1_missing_labels"
    return YoloDatasetLoader.load(dataset_dir)


@pytest.fixture
def invalid_dataset_empty_train_images():
    root = Path("tests/data").resolve()
    dataset_dir = root / "yolo_invalid_dataset1_missing_train_images"
    return YoloDatasetLoader.load(dataset_dir)

@pytest.fixture
def invalid_dataset_missing_train_images(fake_dataset1, tmp_path):
    missing = tmp_path / "does_not_exist"

    return YoloDataset(
        root=fake_dataset1.root,
        train_images=missing,  # ❌
        train_labels=fake_dataset1.train_labels,
        val_images=fake_dataset1.val_images,
        val_labels=fake_dataset1.val_labels,
        test_images=fake_dataset1.test_images,
        test_labels=fake_dataset1.test_labels,
        yaml_path=fake_dataset1.yaml_path,
        num_classes=2,
        class_names=("cat", "dog"),
    )



# --- Tests ---

# - valid

def test_validate_all_valid_dataset(fake_dataset1):
    validator = YoloDatasetValidator(fake_dataset1)
    # darf keine Exception werfen
    validator.validate("all")

@pytest.mark.parametrize("split", ["train", "val", "test"])
def test_validate_single_split_valid(fake_dataset1, split):
    validator = YoloDatasetValidator(fake_dataset1)
    # darf keine Exception werfen
    validator.validate(split)

# - invalid
def test_validate_train_missing_labels_path_raises(invalid_dataset_no_train_labels_path):
    validator = YoloDatasetValidator(invalid_dataset_no_train_labels_path)
    with pytest.raises(ValueError, match="Split 'train' hat keinen Label-Pfad"):
        validator.validate("train")


def test_validate_all_fails_if_train_labels_path_missing(invalid_dataset_no_train_labels_path):
    validator = YoloDatasetValidator(invalid_dataset_no_train_labels_path)
    with pytest.raises(ValueError):
        validator.validate("all")


def test_validate_train_empty_labels_raises(invalid_dataset_empty_train_labels):
    validator = YoloDatasetValidator(invalid_dataset_empty_train_labels)
    with pytest.raises(ValueError, match="Keine Labels.*train"):
        validator.validate("train")


