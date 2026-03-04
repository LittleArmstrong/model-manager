from dataclasses import dataclass
from ultralytics import YOLO
from typing import List, Dict
from pathlib import Path
import logging 

logger = logging.getLogger(__name__)


@dataclass
class YoloModelInfo:
    name: str                 # yolov10 / yolov11 / yolov12
    size: str                    # n, s, m, l, x
    backbone_stages: int
    head_stages: int
    max_freeze: int


class YoloModelInspector:
    """
    Liefert strukturierte Infos zur YOLO-Modellarchitektur
    (Freeze-relevant, GUI-tauglich)
    """

    @staticmethod
    def inspect(model: YOLO) -> YoloModelInfo:
        yaml = model.model.yaml

        # --- Version bestimmen ---
        yaml_file = Path(yaml.get("yaml_file", ""))
        raw_name = yaml_file.stem[:-1].lower()
        size = yaml_file.stem[-1:].lower()

        # yolo11 -> yolov11
        if raw_name.startswith("yolo") and raw_name[4:].isdigit():
            name = f"yolov{raw_name[4:]}"
        else:
            name = raw_name

        # --- Backbone / Head aus YAML ---
        backbone_len = len(yaml.get("backbone", []))
        head_len = len( yaml.get("head", []))
        max_freeze = backbone_len + head_len - 1 # mind. 1 Layer muss trainiert werden

        return YoloModelInfo(
            name=name,
            size=size,
            backbone_stages=backbone_len,
            head_stages=head_len,
            max_freeze=max_freeze
        )

