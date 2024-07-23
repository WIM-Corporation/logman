from loguru import logger, _Logger
from typing import Dict
import json
import threading


class LoggerFactory:
    _loggers: Dict[str, _Logger] = {}
    _lock = threading.Lock()  # 스레드 안전성 보장
    _initialized = False  # 로깅 설정 초기화 여부

    @classmethod
    def _initialize_logging(cls):
        if not cls._initialized:
            with cls._lock:
                if not cls._initialized:  # 이중 체크 잠금
                    logger.remove()  # 기본 설정 제거

                    # JSON 포맷터 정의
                    def serialize(record):
                        print("========================================")
                        print(record["time"])
                        print()
                        print("========================================")

                        log_record = {
                            "timestamp": record["time"].strftime(
                                "%Y-%m-%d %H:%M:%S.%f"
                            )[:-3],
                            "name": record["extra"].get("name", "default"),
                            "level": record["level"].name,
                            "message": record["message"],
                            # "file": record["file"].path,
                            # "function": record["function"],
                            # "line": record["line"],
                            # "module": record["module"],
                            "thread": record["thread"].name,
                            # "process": record["process"].name,
                        }
                        if record["exception"] is not None:
                            log_record["exception"] = {
                                "type": record["exception"].type.__name__,
                                "value": str(record["exception"].value),
                                "traceback": str(record["exception"].traceback),
                            }
                        return json.dumps(log_record, ensure_ascii=False)

                    def patching(record):
                        record["extra"]["serialized"] = serialize(record)

                    logger.patch(patching)

                    # JSON 포맷으로 info.log를 기록하는 핸들러 추가
                    logger.add(
                        "info.log",
                        format=serialize,
                        level="INFO",
                        rotation="00:00",  # 매일 자정에 회전
                        retention="30 days",  # 30일 동안 보관
                        compression="zip",  # 압축
                        enqueue=True,  # 비동기 처리
                        serialize=True,  # JSON 직렬화
                    )

                    # JSON 포맷으로 error.log를 기록하는 핸들러 추가
                    logger.add(
                        "error.log",
                        format="{extra[serialized]}",
                        level="ERROR",
                        rotation="00:00",  # 매일 자정에 회전
                        retention="30 days",  # 30일 동안 보관
                        compression="zip",  # 압축
                        enqueue=True,  # 비동기 처리
                        serialize=True,  # JSON 직렬화
                    )

                    cls._initialized = True

    @classmethod
    def getLogger(cls, name) -> _Logger:
        cls._initialize_logging()
        if name not in cls._loggers:
            with cls._lock:
                if name not in cls._loggers:  # 두 번째 확인 (double-checked locking)
                    cls._loggers[name] = logger.bind(name=name)
        return cls._loggers[name]
