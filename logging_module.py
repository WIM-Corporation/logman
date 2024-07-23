import logging
import logging.handlers
import json
import threading
import time
from typing import Dict


class JsonFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        if datefmt:
            return super().formatTime(record, datefmt)
        ct = self.converter(record.created)
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
        return s

    def format(self, record):
        print("==============================")
        print(record)
        print(record.exc_info)
        print("==============================")
        log_record = {
            "context": record.name,
            "level": record.levelname,
            "timestamp": self.formatTime(record, self.datefmt),
            "message": record.getMessage(),
            "thread": f"{record.threadName}-{record.thread}",
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)


class LoggerFactory:
    _loggers: Dict[str, logging.Logger] = {}
    _lock = threading.Lock()  # 스레드 안전성 보장
    _initialized = False  # 로깅 설정 초기화 여부

    @classmethod
    def _initialize_logging(cls):
        if not cls._initialized:
            with cls._lock:
                if not cls._initialized:  # 이중 체크 잠금
                    logging.basicConfig(level=logging.DEBUG)  # 기본 설정 제거

                    # JSON 포맷터 정의
                    json_formatter = JsonFormatter()

                    # INFO 레벨 핸들러 설정
                    info_handler = logging.handlers.TimedRotatingFileHandler(
                        "info.log", when="midnight", backupCount=30
                    )
                    info_handler.setLevel(logging.INFO)
                    info_handler.setFormatter(json_formatter)
                    info_handler.suffix = "%Y-%m-%d"
                    cls._add_handler(info_handler)

                    # ERROR 레벨 핸들러 설정
                    error_handler = logging.handlers.TimedRotatingFileHandler(
                        "error.log", when="midnight", backupCount=30
                    )
                    error_handler.setLevel(logging.ERROR)
                    error_handler.setFormatter(json_formatter)
                    error_handler.suffix = "%Y-%m-%d"
                    cls._add_handler(error_handler)

                    cls._initialized = True

    @classmethod
    def _add_handler(cls, handler):
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)

    @classmethod
    def getLogger(cls, name) -> logging.Logger:
        cls._initialize_logging()
        if name not in cls._loggers:
            with cls._lock:
                if name not in cls._loggers:  # 두 번째 확인 (double-checked locking)
                    cls._loggers[name] = logging.getLogger(name)
        return cls._loggers[name]


# 사용 예시
logger = LoggerFactory.getLogger("my_logger")
logger.info("This is an info message")
logger.error("This is an error message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
