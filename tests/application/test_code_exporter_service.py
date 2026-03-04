from pathlib import Path
from model_manager.application.service.code_exporter_service import CodeExporterService

def test_code_exporter_happy_path(tmp_path: Path):

    target = tmp_path / "code_export"
    CodeExporterService.export(tmp_path)
    assert target.exists()


