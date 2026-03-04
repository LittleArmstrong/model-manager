import pytest
from model_manager.repository.dataset_loader import YoloDatasetLoader, RawDataset
from model_manager.repository.dataset_writer import DatasetWriter, RawDatasetWriter, NewDatasetConfig
import cv2
import numpy as np
import yaml
from PIL import Image
from pathlib import Path

@pytest.fixture
def copied_dataset(tmp_path):
    dataset = YoloDatasetLoader.load("tests/data/yolo_dataset1")
    writer = DatasetWriter(dataset)
    dst = writer.copy_dataset(tmp_path / "copied_ds")
    return YoloDatasetLoader.load(dst)


# --- Tests
# - DatasetWriter
def test_copy_dataset(tmp_path):
    dataset = YoloDatasetLoader.load("tests/data/yolo_dataset1")
    writer = DatasetWriter(dataset)
    dst = tmp_path / "copied_ds"
    new_root = writer.copy_dataset(dst)

    assert new_root.exists()
    assert (new_root / "images").exists()
    assert (new_root / "labels").exists()
    assert (new_root / "data.yaml").exists()

def test_copy_dataset_with_loader(tmp_path):
    dataset = YoloDatasetLoader.load("tests/data/yolo_dataset1")
    writer = DatasetWriter(dataset)
    dst = tmp_path / "copied_ds"

    # Loader übergeben -> neuer Writer
    new_writer = writer.copy_dataset(dst, loader=YoloDatasetLoader)

    assert isinstance(new_writer, DatasetWriter)
    assert new_writer.dataset.root.exists()
    assert (new_writer.dataset.root / "images").exists()
    assert (new_writer.dataset.root / "labels").exists()
    assert (new_writer.dataset.root / "data.yaml").exists()



def test_save_image(copied_dataset):
    writer = DatasetWriter(copied_dataset)
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    path = writer.save_image("train", "test_img.jpg", img)
    assert path.exists()
    loaded = cv2.imread(str(path))
    assert loaded.shape == (10, 10, 3)

def test_save_label(copied_dataset):
    writer = DatasetWriter(copied_dataset)
    boxes = [[0.5, 0.5, 0.2, 0.2]]
    classes = [1]

    path = writer.save_label("train", "test_label.txt", boxes, classes)

    assert path.exists()

    content = path.read_text().strip()
    assert content == "1 0.500000 0.500000 0.200000 0.200000"



def test_save_yaml(copied_dataset):
    writer = DatasetWriter(copied_dataset)
    data = {
        "train": "images/train",
        "val": "images/val",
        "names": ["a", "b"],
        "nc": 2,
    }
    writer.save_yaml(data)
    loaded = yaml.safe_load(writer.dataset.yaml_path.read_text(encoding="utf-8-sig"))
    assert loaded == data


# - RawDatasetWriter
def test_raw_dataset_writer_write_yolo_train_split(tmp_path: Path):
    # -------------------------------------------------
    # Setup: Fake Raw-Paare
    # -------------------------------------------------
    img_dir = tmp_path / "images"
    lbl_dir = tmp_path / "labels"
    img_dir.mkdir()
    lbl_dir.mkdir()

    img1 = img_dir / "a.png"
    img2 = img_dir / "b.png"
    img3 = img_dir / "c.png"
    lbl1 = lbl_dir / "a.txt"
    lbl2 = lbl_dir / "b.txt"
    lbl3 = lbl_dir / "c.txt"

    Image.new("RGB", (100, 100), color="red").save(img1)
    Image.new("RGB", (200, 200), color="blue").save(img2)
    Image.new("RGB", (150, 150), color="gray").save(img3)
    lbl1.write_text("0 0.5 0.5 1.0 1.0")
    lbl2.write_text("1 0.5 0.5 1.0 1.0")
    lbl3.write_text("2 0.5 0.5 1.0 1.0")

    pairs = [
        (img1, lbl1),
        (img2, lbl2), 
        (img3, lbl3), 
    ]
    raw_ds = RawDataset(root=tmp_path, image_dirs=(img_dir,), label_dirs=(lbl_dir,))
    imgsz = 64
    # -------------------------------------------------
    # Writer
    # -------------------------------------------------
    out = tmp_path / "out"
    writer = RawDatasetWriter(raw_ds)
    class_names = ["a", "b", "c"]
    cfg = NewDatasetConfig(out,pairs, class_names, imgsz, train_size=1.0)
    writer.save_as_dataset(cfg)

    # -------------------------------------------------
    # Assertions: Images
    # -------------------------------------------------
    out_img1 = out / "images" / "train" / "a.png"
    out_img2 = out / "images" / "train" / "b.png"
    out_img3 = out / "images" / "train" / "c.png"

    assert out_img1.exists()
    assert out_img2.exists()
    assert out_img3.exists()

    img = Image.open(out_img1)
    assert img.size == (64, 64)

    assert (out / "data.yaml").exists()

    # -------------------------------------------------
    # Assertions: Labels
    # -------------------------------------------------
    out_lbl1 = out / "labels" / "train" / "a.txt"
    out_lbl2 = out / "labels" / "train" / "b.txt"
    out_lbl3 = out / "labels" / "train" / "c.txt"

    assert out_lbl1.exists()
    assert out_lbl2.exists()  
    assert out_lbl3.exists()  

def test_raw_dataset_writer_write_yolo_all_splits(tmp_path: Path):
    # -------------------------------------------------
    # Setup: Fake Raw-Paare
    # -------------------------------------------------
    img_dir = tmp_path / "images"
    lbl_dir = tmp_path / "labels"
    img_dir.mkdir()
    lbl_dir.mkdir()

    img1 = img_dir / "a.png"
    img2 = img_dir / "b.png"
    img3 = img_dir / "c.png"
    lbl1 = lbl_dir / "a.txt"
    lbl2 = lbl_dir / "b.txt"
    lbl3 = lbl_dir / "c.txt"

    Image.new("RGB", (100, 100), color="red").save(img1)
    Image.new("RGB", (200, 200), color="blue").save(img2)
    Image.new("RGB", (150, 150), color="gray").save(img3)
    lbl1.write_text("0 0.5 0.5 1.0 1.0")
    lbl2.write_text("1 0.5 0.5 1.0 1.0")
    lbl3.write_text("2 0.5 0.5 1.0 1.0")

    pairs = [
        (img1, lbl1),
        (img2, lbl2), 
        (img3, lbl3), 
    ]
    raw_ds = RawDataset(root=tmp_path, image_dirs=(img_dir,), label_dirs=(lbl_dir,))
    imgsz = 64
    # -------------------------------------------------
    # Writer
    # -------------------------------------------------
    out = tmp_path / "out"
    writer = RawDatasetWriter(raw_ds)
    class_names = ["a", "b", "c"]
    cfg = NewDatasetConfig(out,pairs, class_names, imgsz, train_size=0.34, val_size=0.33, test_size=0.33)
    writer.save_as_dataset(cfg)

    # -------------------------------------------------
    # Assertions
    # -------------------------------------------------
    img_total = 0
    lbl_total = 0
    for split in ("train", "val", "test"):
        img_folder = out / "images" / split
        lbl_folder = out / "labels" / split
        assert img_folder.exists()
        assert lbl_folder.exists()

        imgs = list((img_folder).iterdir())
        lbls = list((lbl_folder).iterdir())

        img_count = len(imgs) 
        lbl_count = len(lbls)
        assert img_count == 1
        assert lbl_count == 1
        img_total += img_count
        lbl_total += lbl_count
    
    assert img_total == 3
    assert lbl_total == 3

def test_raw_dataset_writer_write_yolo_train_val_splits(tmp_path: Path):
    # -------------------------------------------------
    # Setup: Fake Raw-Paare
    # -------------------------------------------------
    img_dir = tmp_path / "images"
    lbl_dir = tmp_path / "labels"
    img_dir.mkdir()
    lbl_dir.mkdir()

    img1 = img_dir / "a.png"
    img2 = img_dir / "b.png"
    img3 = img_dir / "c.png"
    lbl1 = lbl_dir / "a.txt"
    lbl2 = lbl_dir / "b.txt"
    lbl3 = lbl_dir / "c.txt"

    Image.new("RGB", (100, 100), color="red").save(img1)
    Image.new("RGB", (200, 200), color="blue").save(img2)
    Image.new("RGB", (150, 150), color="gray").save(img3)
    lbl1.write_text("0 0.5 0.5 1.0 1.0")
    lbl2.write_text("1 0.5 0.5 1.0 1.0")
    lbl3.write_text("2 0.5 0.5 1.0 1.0")

    pairs = [
        (img1, lbl1),
        (img2, lbl2), 
        (img3, lbl3), 
    ]
    raw_ds = RawDataset(root=tmp_path, image_dirs=(img_dir,), label_dirs=(lbl_dir,))
    imgsz = 64
    # -------------------------------------------------
    # Writer
    # -------------------------------------------------
    out = tmp_path / "out"
    writer = RawDatasetWriter(raw_ds)
    class_names = ["a", "b", "c"]
    cfg = NewDatasetConfig(out,pairs, class_names, imgsz, train_size=0.67, val_size=0.33)
    writer.save_as_dataset(cfg)

    # -------------------------------------------------
    # Assertions
    # -------------------------------------------------
    img_total = 0
    lbl_total = 0
    for count, split in ((2, "train"), (1, "val")):
        img_folder = out / "images" / split
        lbl_folder = out / "labels" / split
        assert img_folder.exists()
        assert lbl_folder.exists()

        imgs = list((img_folder).iterdir())
        lbls = list((lbl_folder).iterdir())

        img_count = len(imgs) 
        lbl_count = len(lbls)
        assert img_count == count
        assert lbl_count == count
        img_total += img_count
        lbl_total += lbl_count
    
    assert img_total == 3
    assert lbl_total == 3


def test_new_dataset_config_validation(tmp_path:Path):
    with pytest.raises(ValueError):
        cfg = NewDatasetConfig(tmp_path, [(tmp_path/"a.png", tmp_path / "a.txt")], ["a"], train_size=-0.5)
        cfg.validate()

    with pytest.raises(ValueError):
        cfg = NewDatasetConfig(tmp_path, [(tmp_path/"a.png", tmp_path / "a.txt")], ["a"], train_size=1.5)
        cfg.validate()

    with pytest.raises(ValueError):
        cfg = NewDatasetConfig(tmp_path, [(tmp_path/"a.png", tmp_path / "a.txt")], ["a"], train_size=0.5, val_size=0.6)
        cfg.validate()