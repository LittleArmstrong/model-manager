import numpy as np
from pathlib import Path
import pytest

from model_manager.application.service.predictions_service import draw_predictions_on_image


def test_draw_predictions_returns_png_bytes(mocker):
    fake_img = np.zeros((50, 50, 3), dtype=np.uint8)

    mocker.patch(
        "model_manager.repository.dataset_reader.DatasetReader.load_image",
        return_value=fake_img
    )

    result = draw_predictions_on_image(
        prediction={
            "file_name": "img.jpg",
            "category_ids": [1],
            "scores": [0.9],
            "bboxes": [[1, 1, 10, 10]],
            "min_score": 0.9,
            "max_score": 0.9,
        },
        image_folder=Path("/fake"),
        class_names={0: "cat"}
    )

    assert isinstance(result, bytes)
    assert len(result) > 0


def test_draw_predictions_returns_empty_bytes_if_image_missing(mocker):
    mocker.patch(
        "model_manager.repository.dataset_reader.DatasetReader.load_image",
        return_value=None
    )

    result = draw_predictions_on_image(
        prediction={"file_name": "missing.jpg"},
        image_folder=Path("/fake/images"),
        class_names={}
    )

    assert result == b""
