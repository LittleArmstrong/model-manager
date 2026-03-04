from pathlib import Path
from model_manager.repository.dataset_loader import RawDatasetLoader
from model_manager.repository.dataset_reader import RawDatasetReader
from model_manager.repository.dataset_writer import RawDatasetWriter, NewDatasetConfig
from typing import Callable

class DatasetCreationService:

    def __init__(self):
        self._cancel = False

    def generate_dataset(
        self,
        source_path: str,
        target_path: str,
        dataset_name: str,
        class_names: list[str],
        imgsz: int,
        train_size: float,
        val_size: float,
        test_size: float,
        progress_callback: Callable[[int, int], None]=None
        ):
        
        out = Path(target_path) / dataset_name
        raw_ds = RawDatasetLoader.load(Path(source_path))
        ds_reader = RawDatasetReader(raw_ds)
        writer = RawDatasetWriter(raw_ds)

        pairs = list(ds_reader.iter_pairs())
        cfg = NewDatasetConfig(out, pairs, class_names, imgsz, train_size, val_size, test_size)
        cfg.validate()
        writer.save_as_dataset(cfg, progress_callback, self._abort_if_cancelled)

        return out
    
    def _abort_if_cancelled(self, *args, **kwargs):
        if self._cancel:
            raise StopIteration("Cancel")
        
    def cancel(self):
        self._cancel = True

    

