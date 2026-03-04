from pathlib import Path
import shutil
from model_manager.core.utils import resource_path

class CodeExporterService:
    @staticmethod
    def export(target_path: str):
        target_path = Path(target_path) / "code_export"
        template_path = resource_path("code_export_template", internal=True)
        shutil.copytree(template_path, target_path)