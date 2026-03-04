from ultralytics import YOLO
from pathlib import Path
import shutil
import logging

logger = logging.getLogger(__name__)


class YoloModelExporter:
    def __init__(self, model: YOLO):
        self.model = model

    def export(self, target: Path, fmt: str | None = None) -> Path:
        """
        Exportiert ein YOLO-Modell und verschiebt es an den gewünschten Ort.

        :param target: Zielpfad inkl. Dateiname
        :param fmt: 'onnx',  None (= PyTorch)
        :return: Finaler Speicherpfad
        """
        if fmt:
            exported = Path(self.model.export(format=fmt))
            target = target.with_suffix(exported.suffix)

            try:
                shutil.move(exported, target)
            except Exception as e:
                logger.exception(e)
                if exported.exists() and fmt:
                    exported.unlink()
                return None
        else:
            target = target.with_suffix(".pt")
            self.model.save(target)
        return target

        