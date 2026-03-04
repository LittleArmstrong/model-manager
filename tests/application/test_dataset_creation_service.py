from pathlib import Path
from model_manager.application.service.dataset_creation_service import DatasetCreationService
import yaml

def test_generate_dataset_integration(tmp_path):
    # Quell-Dataset: bestehender Testdatensatz
    source_path = Path("tests/data/raw_dataset")  # sollte existieren mit Bildern
    target_path = tmp_path
    dataset_name = "test_ds"
    class_names = ["class1", "class2"]
    imgsz = 416

    # Split-Größen
    train_size = 0.6
    val_size = 0.2
    test_size = 0.2

    # Dataset erzeugen
    out_dir = DatasetCreationService.generate_dataset(
        source_path=str(source_path),
        target_path=str(target_path),
        dataset_name=dataset_name,
        class_names=class_names,
        imgsz=imgsz,
        train_size=train_size,
        val_size=val_size,
        test_size=test_size
    )

    # Prüfen, dass das Datasetverzeichnis erstellt wurde
    assert out_dir.exists()
    assert (out_dir / "images").exists()
    assert (out_dir / "labels").exists()
    assert (out_dir / "data.yaml").exists()

    # Prüfen, dass Bilder kopiert wurden
    train_images = list((out_dir / "images" / "train").glob("*"))
    val_images = list((out_dir / "images" / "val").glob("*"))
    test_images = list((out_dir / "images" / "test").glob("*"))

    assert len(train_images) > 0
    assert len(val_images) > 0
    assert len(test_images) > 0

    # Prüfen, dass Labels existieren
    for img_path in train_images + val_images + test_images:
        label_path = Path(str(img_path).replace("images", "labels")).with_suffix(".txt")
        assert label_path.exists()

    # Prüfen, dass data.yaml korrekt ist

    yaml_path = out_dir / "data.yaml"
    with open(yaml_path) as f:
        cfg = yaml.safe_load(f)
    assert cfg["names"] == class_names
    assert cfg["train"] == "images/train"
    assert cfg["val"] == "images/val"
    assert cfg["test"] == "images/test"
    assert cfg["nc"] == 2
