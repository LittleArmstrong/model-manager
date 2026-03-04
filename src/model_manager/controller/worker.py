import PySide6.QtCore as qtc
from typing import Callable, Optional
import logging
logger = logging.getLogger(__name__)


class Worker(qtc.QThread):
    finished = qtc.Signal(object)  # Result
    error = qtc.Signal(str)

    def __init__(self, task: Callable, *args, **kwargs):
        super().__init__()
        self.task = task
        self.args = args
        self.kwargs = kwargs

    @qtc.Slot()
    def run(self):
        try:
            result = self.task(
                *self.args,
                **self.kwargs
            )
            self.finished.emit(result)
        except Exception as e:
            logger.exception(e)
            self.error.emit(str(e))
            self.finished.emit(None)

    @classmethod
    def start_task(cls,task: Callable, *args, finished_cb: Optional[Callable] = None, error_cb: Optional[Callable] = None,  **kwargs):
        worker = cls(task, *args, **kwargs)
        if finished_cb:
            worker.finished.connect(finished_cb)
        if error_cb:
            worker.error.connect(error_cb)
        worker.start()
        return worker