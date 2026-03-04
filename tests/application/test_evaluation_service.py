import numpy as np
from pathlib import Path
import pytest

from model_manager.application.service.evaluation_service import YoloEvaluationService


def test_evaluation_service_happy_path(mocker):
    # Arrange
    fake_dataset = mocker.Mock()
    fake_result = mocker.Mock()

    mocker.patch(
        "model_manager.repository.dataset_loader.YoloDatasetLoader.load",
        return_value=fake_dataset
    )
    mocker.patch(
        "model_manager.domain.services.dataset_validator.YoloDatasetValidator.validate",
        return_value = True
    )
    mocker.patch(
        "model_manager.repository.model_loader.YoloModelLoader.load",
        return_value=mocker.Mock()
    )
    test_mock = mocker.patch(
        "model_manager.domain.services.model_tester.YoloModelTester.test",
        return_value=fake_result
    )

    service = YoloEvaluationService(
        dataset_path="fake/path",
        model_weights_path="fake.pt"
    )

    # Act
    result = service.start_testing()

    # Assert
    assert result is fake_result
    test_mock.assert_called_once()

def test_dataset_error_triggers_callback(mocker):
    mocker.patch(
        "model_manager.repository.dataset_loader.YoloDatasetLoader.load",
        side_effect=Exception("dataset kaputt")
    )

    on_error = mocker.Mock()

    service = YoloEvaluationService(
        dataset_path="fake/path",
        on_error=[on_error]
    )

    result = service.start_testing()

    assert result is None
    on_error.assert_called_once()
    message = on_error.call_args.args[0]
    assert "Ungültiger Datensatz" in message
    assert "dataset kaputt" in message

def test_cancel_triggers_on_test_canceled(mocker):
    fake_dataset = mocker.Mock()

    mocker.patch(
        "model_manager.repository.dataset_loader.YoloDatasetLoader.load",
        return_value=fake_dataset
    )
    mocker.patch(
        "model_manager.domain.services.dataset_validator.YoloDatasetValidator.validate"
    )
    mocker.patch(
        "model_manager.repository.model_loader.YoloModelLoader.load",
        return_value=mocker.Mock()
    )

    mocker.patch(
        "model_manager.domain.services.model_tester.YoloModelTester.test",
        side_effect=StopIteration
    )

    on_canceled = mocker.Mock()

    service = YoloEvaluationService(
        dataset_path="fake/path",
        on_error=[on_canceled]
    )

    result = service.start_testing()

    assert result is None
    on_canceled.assert_called_once()
    message = on_canceled.call_args.args[0]
    assert "Test wurde abgebrochen!" in message
