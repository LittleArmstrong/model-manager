import pytest
from unittest.mock import Mock

from model_manager.application.service.training_service import YoloTrainingService
from model_manager.domain.services.model_trainer import TrainingResults


def test_training_service_happy_path(monkeypatch):
    # ---------- Arrange ----------
    fake_dataset = Mock()
    fake_model = Mock()
    fake_result = Mock(spec=TrainingResults)

    # DatasetLoader
    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloDatasetLoader.load",
        lambda path: fake_dataset
    )

    # DatasetValidator
    fake_validator = Mock()
    fake_validator.validate = Mock()

    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloDatasetValidator",
        lambda dataset: fake_validator
    )

    # ModelLoader
    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloModelLoader.load",
        lambda *_: fake_model
    )

    # ModelTrainer
    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloModelTrainer.train",
        lambda *args, **kwargs: fake_result
    )

    error_cb = Mock()

    service = YoloTrainingService(
        dataset_path="fake/path",
        model_name="yolov8",
        model_size="n",
        pretrained=True,
        apply_transfer_learning=False,
        freeze=0,
        imgsz=640,
        batch=4,
        epochs=1,
        optimizer="auto",
        lr0=0.01,
        weight_decay=0.0001,
        on_error=error_cb,
    )

    # ---------- Act ----------
    result = service.start_training()

    # ---------- Assert ----------
    assert result is fake_result
    fake_validator.validate.assert_any_call(split="train")
    fake_validator.validate.assert_any_call(split="val")
    error_cb.assert_not_called()



def test_training_service_dataset_invalid(monkeypatch):
    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloDatasetLoader.load",
        lambda _: Mock()
    )

    def validator_fail(_):
        v = Mock()
        v.validate.side_effect = ValueError("invalid dataset")
        return v

    monkeypatch.setattr(
        "model_manager.application.service.training_service.YoloDatasetValidator",
        validator_fail
    )

    error_cb = Mock()

    service = YoloTrainingService(
        dataset_path="fake/path",
        model_name="yolov8",
        model_size="n",
        pretrained=True,
        apply_transfer_learning=False,
        freeze=0,
        imgsz=640,
        batch=4,
        epochs=1,
        optimizer="auto",
        lr0=0.01,
        weight_decay=0.0001,
        on_error=[error_cb],
    )

    result = service.start_training()

    assert result is None
    error_cb.assert_called_once()
