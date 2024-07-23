import logging
import os

from typing import Union


class FileRotateLoggingHandler(logging.handlers.RotatingFileHandler):
    def __init__(
        self,
        formatter: logging.Formatter,
        filePath: Union[str, os.PathLike[str]],
        maxBytes: int,
        level: int = logging.DEBUG,
    ):
        if not os.path.exists(os.path.dirname(filePath)):
            os.makedirs(os.path.dirname(filePath))

        super().__init__(
            filePath,
            maxBytes=maxBytes,
            backupCount=10,
            encoding="utf-8",
        )
        self.setLevel(level)
        self.setFormatter(formatter)
