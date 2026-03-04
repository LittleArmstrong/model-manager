import sys
import os
import pathlib


if sys.platform == "win32":
   import ctypes
   APP_ID = "th-cologne.master.model_manager"  # beliebig, aber eindeutig!
   ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


# ---------------------------------------------------
# fix ultralytics pathlib error
sys.modules["pathlib._local"] = pathlib 
if os.name == 'nt':
   pathlib.PosixPath = pathlib.WindowsPath
else:
   pathlib.WindowsPath = pathlib.PosixPath

# fix ultralytics write error on no console build
from model_manager.core.utils import is_frozen
if is_frozen():
   sys.stdout = open(os.devnull, "w")
   sys.stderr = open(os.devnull, "w")
# ---------------------------------------------------

import logging
from model_manager.core.logging_config import setup_logging
setup_logging()

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from model_manager.controller.main_controller import MainController
from model_manager.core.utils import resource_path


logger = logging.getLogger(__name__)
def main():
   logger.debug("Start")
   
   app = QApplication(sys.argv)
   app.setApplicationName("Model Manager")
   app.setOrganizationName("TH Cologne")
   app.setWindowIcon(QIcon(str(resource_path("logo.ico", internal=True))))
   app.setStyle("Fusion")

   main_controller = MainController()
   main_controller.view.show()


   logger.info("GUI geöffnet.")

   status_code = app.exec()
   logger.info("GUI beendet.")
   sys.exit(status_code)

if __name__ == "__main__":
   main()