
from pathlib import Path
import logging
import cv2
from ultralytics.utils.plotting import Annotator
from model_manager.repository.dataset_reader import DatasetReader


def draw_predictions_on_image(prediction: dict, image_folder: Path, class_names: dict) -> bytes:
    """
    Lädt ein Bild und zeichnet die Bounding Boxes und Scores der Predictions
    mit YOLO Annotator. Gibt ein PNG-Bytearray zurück, das direkt in QPixmap.loadFromData() verwendet werden kann.

    Args:
        info (dict): Prediction-Info für ein Bild, z.B.:
            {
                "file_name": "000000000042.jpg",
                "category_ids": [17],
                "scores": [0.7649],
                "bboxes": [[226.904, 42.66, 346.959, 251.881]],
                "min_score": 0.7649,
                "max_score": 0.7649
            }
        image_folder (Path): Ordner mit Testbildern
        class_names (dict): mapping class_id → class_name

    Returns:
        bytes: PNG-codiertes Bild, kompatibel mit QPixmap.loadFromData()
    """
    img = DatasetReader.load_image(image_folder / prediction["file_name"]) 
    if img is None:
        return b""

    annotator = Annotator(img)

    for bbox, score, cat_id in zip(prediction["bboxes"], prediction["scores"], prediction["category_ids"]):
        # YOLO Annotator erwartet [x1, y1, x2, y2]
        x, y, w, h = bbox
        xyxy = [x, y, x + w, y + h]
        class_name = class_names.get(cat_id-1, str(cat_id-1))
        annotator.box_label(xyxy, f"{class_name} {score:.2f}")

    img_annotated = annotator.result()

    # In PNG-Bytes konvertieren für QPixmap
    success, buf = cv2.imencode(".png", cv2.cvtColor(img_annotated, cv2.COLOR_RGB2BGR))
    if not success:
        return b""
    return buf.tobytes()