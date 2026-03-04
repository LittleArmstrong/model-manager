import logging.config
from pathlib import Path
import os
from model_manager.core.utils import resource_path, is_frozen
import sys


# LOG_DIR_NAME = "logs"
# LOG_DIR = Path(os.getenv("PROJECT_ROOT", os.getcwd())) / LOG_DIR_NAME
# os.makedirs(LOG_DIR, exist_ok=True)
LOG_DIR = resource_path("logs", relative=True)
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE_NAME = "app.log"
LOG_FILE_PATH = LOG_DIR / LOG_FILE_NAME


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "console": {
            "format": "[%(levelname)s] %(name)s: %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d) - %(message)s"
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",              # Console kann alles anzeigen
            "formatter": "console",
        },
        "file_debug": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",              # Datei erhält volle Infos
            "filename": str(LOG_FILE_PATH),
            "maxBytes": 10_000_000,
            "backupCount": 5,
            "encoding": "utf8",
            "formatter": "detailed",
        },
    },

    "loggers": {
        # ---------------------------
        # Dein eigener Logger
        # ---------------------------
        "model_manager": {
            "level": "DEBUG",
            "handlers": ["console", "file_debug"],
            "propagate": False,
        },

        # ---------------------------
        # Frameworks → nur INFO+
        # ---------------------------
        "ultralytics": {"level": "INFO"},
        "torch":       {"level": "INFO"},
        "matplotlib":  {"level": "INFO"},
        "PIL":         {"level": "INFO"},
        "asyncio":     {"level": "WARNING"},
        "uvicorn":     {"level": "WARNING"},
    },

    # Root-Logger → blockiert Debug der Welt
    "root": {
        "level": "INFO",
        "handlers": ["console", "file_debug"],
    },
}


def setup_logging():
    config = LOGGING_CONFIG.copy()
    if is_frozen():
        config["handlers"].pop("console", None)
        config["root"]["handlers"] = ["file_debug"]
        config["loggers"]["model_manager"]["handlers"] = ["file_debug"]

    logging.config.dictConfig(config)