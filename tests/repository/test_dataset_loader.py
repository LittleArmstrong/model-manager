import pytest
from pathlib import Path
import numpy as np
import cv2
import yaml

from model_manager.repository.dataset_loader import YoloDatasetLoader, YoloDataset

# --- Fixtures ---

@pytest.fixture
def fake_dataset1():
    # Dummy Dataset Struktur
    root = Path("tests/data").resolve()
    dataset_dir = root / "yolo_dataset1"
    images_dir = dataset_dir / "images"
    labels_dir = dataset_dir / "labels"

    train_images = images_dir / "train" 
    train_labels = labels_dir / "train" 
    val_images = images_dir / "val" 
    val_labels = labels_dir / "val" 
    test_images = images_dir / "test" 
    test_labels = labels_dir / "test" 
    yaml_path = dataset_dir / "data.yaml"
    return YoloDataset(
        root=dataset_dir,
        train_images=train_images,
        train_labels=train_labels,
        val_images=val_images,
        val_labels=val_labels,
        test_images=test_images,
        test_labels=test_labels,
        yaml_path=yaml_path,
        num_classes=2,
        class_names=("cat", "dog")
    )

# --- Tests ---
# -- YoloDatasetLoader
def test_load_dataset(fake_dataset1):
    dataset = YoloDatasetLoader.load(Path("tests/data/yolo_dataset1"))
    assert dataset == fake_dataset1
    assert dataset.train_images.exists()
    assert dataset.val_images.exists()
    assert dataset.test_images.exists()
    assert dataset.train_labels.exists()

def test_load_dataset_no_folder():
    with pytest.raises(ValueError):
        YoloDatasetLoader.load("tests/data/nonexistent_dataset")

def test_load_dataset_no_yaml(tmp_path):
    # erstelle nur einen Ordner ohne YAML
    empty_dataset = tmp_path / "empty_dataset"
    empty_dataset.mkdir()
    with pytest.raises(FileNotFoundError):
        YoloDatasetLoader.load(empty_dataset)

def test_load_dataset_empty_yaml(tmp_path):
    empty_dataset = tmp_path / "empty_yaml"
    empty_dataset.mkdir()
    yaml_path = empty_dataset / "data.yaml"
    yaml_path.write_text("")  # leere YAML
    with pytest.raises(ValueError):
        YoloDatasetLoader.load(empty_dataset)

def test_load_dataset_multiple_yaml(tmp_path):
    multi_yaml = tmp_path / "multi_yaml"
    multi_yaml.mkdir()
    (multi_yaml / "a.yaml").write_text("train: train")
    (multi_yaml / "b.yaml").write_text("train: train")
    with pytest.raises(ValueError):
        YoloDatasetLoader.load(multi_yaml)


# -- RawDatasetLoader
from model_manager.repository.dataset_loader import RawDatasetLoader, RawDataset
def test_load_raw_dataset_root_images_and_labels(tmp_path: Path):
    # Arrange
    (tmp_path / "img1.png").touch()
    (tmp_path / "img1.txt").touch()
    (tmp_path / "img2.png").touch()
    (tmp_path / "img2.txt").touch()

    # Act
    raw = RawDatasetLoader.load(tmp_path)

    # Assert
    assert isinstance(raw, RawDataset)
    assert raw.root == tmp_path
    assert raw.image_dirs == (tmp_path,)
    assert raw.label_dirs == (tmp_path,)

def test_load_raw_dataset_images_labels_folders(tmp_path: Path):
    images = tmp_path / "images"
    labels = tmp_path / "labels"
    images.mkdir()
    labels.mkdir()

    (images / "a.png").touch()
    (labels / "a.txt").touch()

    raw = RawDatasetLoader.load(tmp_path)

    assert raw.image_dirs == (images,)
    assert raw.label_dirs == (labels,)

def test_load_raw_dataset_random_images_labels_folders(tmp_path: Path):
    images = tmp_path / "random_img"
    labels = tmp_path / "random_lbl"
    images.mkdir()
    labels.mkdir()

    (images / "12sd.png").touch()
    (labels / "12sd.txt").touch()

    raw = RawDatasetLoader.load(tmp_path)

    assert raw.image_dirs == (images,)
    assert raw.label_dirs == (labels,)

def test_load_raw_dataset_no_images_exception(tmp_path: Path):
    images = tmp_path / "random_img"
    labels = tmp_path / "random_lbl"
    images.mkdir()
    labels.mkdir()

    (labels / "12sd.txt").touch()

    with pytest.raises(FileNotFoundError):
        RawDatasetLoader.load(tmp_path)




