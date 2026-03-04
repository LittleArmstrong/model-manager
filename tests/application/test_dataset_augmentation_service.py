from pathlib import Path
from model_manager.application.service.dataset_augmentation_service import AugmentationService
import albumentations as A

def test_augmentation_service_integration_with_existing_dataset(tmp_path):
    src_dir = Path("tests/data/coco8_custom")  # vorhandener valid Dataset
    dst_dir = tmp_path  # temporärer Zielordner

    # Callbacks sammeln
    progress_calls = []
    done_calls = []

    def on_progress(done, total):
        progress_calls.append((done, total))

    def on_done(results):
        done_calls.append(results)

    service = AugmentationService(
        source_dir=str(src_dir),
        output_dir=str(dst_dir),
        dataset_name="ds",
        aug_per_image=2,  # 2 Augmentationen pro Bild
        brightness= 0.2,
        rotation=0, # um bb error zu vermeiden
        translation=0, # um bb error zu vermeiden
        on_progress=on_progress,
        on_done=on_done
    )

    service.augment_dataset()

    # Prüfen, ob Ziel erstellt wurde
    out_dir = dst_dir / "ds"
    assert out_dir.exists()
    assert (out_dir / "images").exists()
    assert (out_dir / "images" / "train" / "000000000009.jpg").exists()
    assert (out_dir / "labels").exists()
    assert (out_dir / "data.yaml").exists()

    # Prüfen, dass augmentierte Bilder existieren
    images = list((out_dir / "images" / "train").glob("*.jpg"))
    assert len(images) == 12  # Es sollten mehr Bilder als original existieren

    # Callbacks wurden gefeuert
    assert len(progress_calls) == 4
    assert len(done_calls) == 1
