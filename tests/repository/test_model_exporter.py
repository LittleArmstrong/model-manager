# test_exporter.py
from pathlib import Path
from pytest_mock import MockerFixture
from model_manager.repository.model_exporter import YoloModelExporter
import pytest

def test_export_model_moves_file_and_returns_target_path(tmp_path: Path, mocker: MockerFixture):
    # Fake exportierte Datei (so als hätte YOLO sie erzeugt)
    exported_file = tmp_path / "model.onnx"
    exported_file.write_text("dummy onnx content")

    # Mock YOLO
    model = mocker.Mock()
    model.export.return_value = str(exported_file)

    exporter = YoloModelExporter(model)

    base_target = tmp_path / "final" 
    base_target.mkdir(parents=True, exist_ok=True)
    target = base_target / "my_model.onnx"
    result = exporter.export(target, fmt="onnx")

    # Assertions
    assert result == target
    assert target.exists()
    assert not exported_file.exists()

    model.export.assert_called_once_with(format="onnx")

def test_export_model_with_no_target_suffix(tmp_path: Path, mocker: MockerFixture):
    # Fake exportierte Datei (so als hätte YOLO sie erzeugt)
    exported_file = tmp_path / "model.onnx"
    exported_file.write_text("dummy onnx content")

    # Mock YOLO
    model = mocker.Mock()
    model.export.return_value = str(exported_file)

    exporter = YoloModelExporter(model)

    base_target = tmp_path / "final" 
    base_target.mkdir(parents=True, exist_ok=True)
    target = base_target / "my_model"
    correct_target = base_target / "my_model.onnx"
    result = exporter.export(target, fmt="onnx")

    # Assertions
    assert result == correct_target
    assert correct_target.exists()
    assert not exported_file.exists()

    model.export.assert_called_once_with(format="onnx")


def test_export_cleanup_on_error(tmp_path: Path, mocker:MockerFixture):
    # Fake exportierte Datei
    exported_file = tmp_path / "model.onnx"
    exported_file.write_text("dummy content")

    # Mock YOLO
    model = mocker.Mock()
    model.export.return_value = str(exported_file)

    mocker.patch("shutil.move", side_effect=RuntimeError("Move failed!"))
    exporter = YoloModelExporter(model)
    exporter.export(target=tmp_path/"a.pt", fmt="onnx")

    assert not exported_file.exists()

def test_export_cleanup_on_pt_export(tmp_path: Path, mocker:MockerFixture):
    # Fake exportierte Datei
    exported_file = tmp_path / "model.pt"
    exported_file.write_text("dummy content")

    # Mock YOLO
    target = tmp_path/"a.pt"
    model = mocker.Mock()
    model.save.side_effect = lambda x: target.write_text("dummy content")
    
    exporter = YoloModelExporter(model)
    exporter.export(target=target, fmt=None)

    assert target.exists()
    assert exported_file.exists()


