from model_manager.repository.model_loader import YoloModelLoader
from model_manager.repository.model_exporter import YoloModelExporter

class YoloModelExporterService:

    @staticmethod    
    def export(target, format, best_model):
        """
        Exportiert das zuletzt trainierte YOLO-Modell und verschiebt es an den gewünschten Ort.

        :param target: Zielpfad inkl. Dateiname
        :param fmt: 'onnx',  None (= PyTorch)
        :return: Finaler Speicherpfad
        """
        last_model = YoloModelLoader.load_last_trained(best_model)
        if not last_model:
            raise FileNotFoundError(f"Kein trainiertes Modell gefunden!")
        return YoloModelExporter(last_model).export(target, format)