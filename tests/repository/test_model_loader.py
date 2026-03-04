import pytest
from pathlib import Path
from ultralytics import YOLO
from unittest.mock import MagicMock, patch

from model_manager.repository.model_loader import (
    YoloModelLoader,
    LoaderConfig,
)


def test_load_with_model_path(mocker):
    model_path = Path("tests/data/n.pt")
    config = LoaderConfig(model_path=model_path)
    yolo_mock = mocker.patch(
        "model_manager.repository.model_loader.YOLO",
        return_value=mocker.Mock()
    )
    model = YoloModelLoader.load(config)
    yolo_mock.assert_called_once_with(model_path)
    assert model is yolo_mock.return_value


def test_load_pretrained_by_name_and_size(mocker):
    mocker.patch(
        "model_manager.repository.model_loader.YoloModelStorage.pretrained_model_path",
        return_value=Path("pretrained.pt")
    )
    yolo_mock = mocker.patch(
        "model_manager.repository.model_loader.YOLO",
        return_value=mocker.Mock()
    )
    config = LoaderConfig(
        model_name="yolov12",
        model_size="s",
        use_pretrained=True,
    )
    model = YoloModelLoader.load(config)
    yolo_mock.assert_called_once_with(Path("pretrained.pt"))
    assert model is yolo_mock.return_value


def test_load_with_weights_path():
    weights_path = Path("tests/data/n.pt")
    config = LoaderConfig(
        model_name="yolov12",
        model_size="n",
        weights_path=weights_path,
    )
    model = YoloModelLoader.load(config)
    assert isinstance(model, YOLO)


def test_load_with_mismatched_weights_raises():
    weights_path = Path("tests/data/n.pt")
    config = LoaderConfig(
        model_name="yolov12",
        model_size="s",
        weights_path=weights_path,
        use_pretrained=False
    )

    with pytest.raises(ValueError):
        YoloModelLoader.load(config)

