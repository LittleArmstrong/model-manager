from model_manager.domain.services.model_tester import YoloModelTester, EvalResult, EvalCallbacks

# -------------------------
# Fakes
# -------------------------

class FakeMetrics:
    def __init__(self):
        self.results_dict = {
            "metrics/precision(B)": 0.8,
            "metrics/recall(B)": 0.6,
            "metrics/mAP50(B)": 0.7,
            "metrics/mAP50-95(B)": 0.5,
        }

    def to_df(self):
        class FakeDF:
            def rows(self, named=True):
                return [
                    {
                        "Class": "class0",
                        "Images": 1,
                        "Instances": 1,
                        "Box-P": 0.8,
                        "Box-R": 0.6,
                        "mAP50": 0.7,
                        "mAP50-95": 0.5,
                    }
                ]
        return FakeDF()

class FakeValidator:
    def __init__(self):
        self.metrics = FakeMetrics()
        self.jdict = [
            {
                "image_id": 0,
                "file_name": "img1.jpg",
                "category_id": 0,
                "score": 0.9,
                "bbox": [10, 10, 100, 100],
            },
            {
                "image_id": 0,
                "file_name": "img1.jpg",
                "category_id": 0,
                "score": 0.85,
                "bbox": [12, 12, 100, 100],
            },
            {
                "image_id": 0,
                "file_name": "img1.jpg",
                "category_id": 0,
                "score": 0.3,  # unter min_conf
                "bbox": [12, 12, 100, 100],
            },
            {
                "image_id": 0,
                "file_name": "img1.jpg",
                "category_id": 1,
                "score": 0.6, 
                "bbox": [12, 12, 10, 10],
            },
            {
                "image_id": 1,
                "file_name": "img2.jpg",
                "category_id": 2,
                "score": 0.7, 
                "bbox": [5, 5, 15, 15],
            },
        ]
        self.callbacks = {
            "on_val_start": [],
            "on_val_batch_start": [],
            "on_val_batch_end": [],
            "on_val_end": [],
        }

    def __call__(self, model=None):
        return None

class FakeDataset:
    yaml_path = "fake.yaml"
    test_images = "fake/path"

class FakeYOLO:
    overrides = {}
    callbacks = {"on_val_batch_end": []}
    names = ["class0"]

    class model:
        pass

# -------------------------
# Test
# -------------------------

def test_yolo_model_tester_returns_test_result(mocker):
    # Arrange
    mocker.patch(
        "model_manager.repository.dataset_reader.DatasetReader.count_images",
        return_value=1
    )

    model = FakeYOLO()
    dataset = FakeDataset()
    fake_validator = FakeValidator()

    # Act
    result = YoloModelTester.test(
        model=model,
        dataset=dataset,
        validator=fake_validator,
        callbacks={}
    )

    # Assert
    assert isinstance(result, EvalResult)
    assert result.img_path == "fake/path"
    assert result.classes == ["class0"]

    assert len(result.metrics) == 2
    assert result.metrics[0]["Class"] == "Gesamt"
    assert result.metrics[1]["Class"] == "class0"

    assert len(result.predictions) == 2
    pred = result.predictions[0]
    assert pred["file_name"] == "img1.jpg"
    assert pred["max_score"] == 0.9
    assert pred["min_score"] == 0.6
    assert pred["bboxes"] == [[10, 10, 100, 100], [12, 12, 10, 10]]
    assert pred["category_ids"] == [0,1]
    assert pred["scores"] == [0.9, 0.6]
    pred = result.predictions[1]
    assert pred["file_name"] == "img2.jpg"
    assert pred["max_score"] == 0.7
    assert pred["min_score"] == 0.7
    assert pred["bboxes"] == [[5, 5, 15, 15]]
    assert pred["category_ids"] == [2]
    assert pred["scores"] == [0.7]

def test_on_val_batch_end_wrapper_receives_total_batches(mocker):
    mocker.patch(
        "model_manager.repository.dataset_reader.DatasetReader.count_images",
        return_value=4
    )

    model = FakeYOLO()
    dataset = FakeDataset()
    fake_validator = FakeValidator()

    on_batch_end = mocker.Mock()

    callbacks = EvalCallbacks(
        on_val_batch_end=[on_batch_end]
    )

    YoloModelTester.test(
        model=model,
        dataset=dataset,
        validator=fake_validator,
        callbacks=callbacks
    )

    # wrapper wird nicht automatisch aufgerufen → manuell triggern
    wrapped_cb = fake_validator.callbacks["on_val_batch_end"][0]
    wrapped_cb(fake_validator)

    on_batch_end.assert_called_once()
    args = on_batch_end.call_args[0]
    assert args[0] is fake_validator
    assert args[1] == 1  # total_batches

