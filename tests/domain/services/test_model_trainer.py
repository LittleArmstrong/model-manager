from model_manager.domain.services.model_trainer import TrainingCallbacks, TrainingConfig, TrainingProgress, TrainingResults, YoloModelTrainer


def test_train_calls_model_train(mocker):
    model = mocker.Mock()
    model.names = ["a", "b"]
    model.reset_callbacks = mocker.Mock()
    model.add_callback = mocker.Mock()

    dataset = mocker.Mock()
    dataset.yaml_path = "data.yaml"

    config = TrainingConfig(epochs=1, batch=2)
    callbacks = TrainingCallbacks()

    # DatasetReader
    mocker.patch(
        "model_manager.domain.services.model_trainer.DatasetReader",
        return_value=mocker.Mock(count_images=lambda split: 4)
    )

    # Inspector
    mocker.patch(
        "model_manager.domain.services.model_trainer.YoloModelInspector.inspect",
        return_value=mocker.Mock(max_freeze=10)
    )

    # Fake train result
    fake_results = mocker.Mock()
    fake_results.results_dict = {
        "metrics/precision(B)": 1.0,
        "metrics/recall(B)": 1.0,
        "metrics/mAP50(B)": 1.0,
        "metrics/mAP50-95(B)": 1.0,
    }
    fake_results.to_df.return_value.rows.return_value = []
    model.train.return_value = fake_results

    result = YoloModelTrainer.train(
        model=model,
        dataset=dataset,
        config=config,
        callbacks=callbacks
    )

    model.train.assert_called_once()
    assert isinstance(result, TrainingResults)

def test_wrap_batch_end_updates_progress(mocker):
    progress = TrainingProgress(
        batches_per_epoch=5,
        total_batches=10,
        epochs=2
    )

    called = {}

    def cb(trainer, prog):
        called["batch"] = prog.batch_count
        called["epoch"] = prog.epoch

    wrapped = YoloModelTrainer._wrap_batch_end(cb, progress)

    trainer = mocker.Mock()
    trainer.epoch = 1

    wrapped(trainer)

    assert progress.batch_count == 1
    assert progress.epoch == 1
    assert called["batch"] == 1


