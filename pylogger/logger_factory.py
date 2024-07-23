import logging
import logging.handlers
import threading
import os

from pylogger.handler import FileRotateLoggingHandler, ConsoleLoggingHandler
from pylogger.formatter import JsonFormatter
from pylogger.custom_logger import CustomLogger
from typing import Dict, List, Union

logging.setLoggerClass(CustomLogger)


class LoggerFactory:
    _filePath: Union[str, os.PathLike[str]] = "logs/app.log"
    _maxBytes: int = 30 * 1024 * 1024
    _loggers: Dict[str, logging.Logger] = {}
    _lock = threading.Lock()  # 스레드 안전성 보장
    _initialized = False  # 로깅 설정 초기화 여부

    @classmethod
    def _initialize_logging(cls):
        if not cls._initialized:
            with cls._lock:
                if not cls._initialized:  # 이중 체크 잠금
                    json_formatter = JsonFormatter()
                    log_level = logging.INFO
                    file_handler = FileRotateLoggingHandler(
                        level=log_level,
                        formatter=json_formatter,
                        maxBytes=cls._maxBytes,
                        filePath=cls._filePath,
                    )
                    console_handler = ConsoleLoggingHandler(
                        level=log_level, formatter=json_formatter
                    )

                    cls._add_handler([file_handler, console_handler])
                    cls._initialized = True

    @classmethod
    def _add_handler(cls, handler: Union[logging.Handler, List[logging.Handler]]):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.NOTSET)  # root 로거의 기본 레벨 설정

        # 기존 핸들러 제거
        if root_logger.hasHandlers():
            root_logger.handlers.clear()

        if isinstance(handler, list):
            for h in handler:
                root_logger.addHandler(h)
        else:
            root_logger.addHandler(handler)

    @classmethod
    def getLogger(cls, name) -> logging.Logger:
        cls._initialize_logging()
        if name not in cls._loggers:
            with cls._lock:
                if name not in cls._loggers:  # 두 번째 확인 (double-checked locking)
                    cls._loggers[name] = logging.getLogger(name)
        return cls._loggers[name]
