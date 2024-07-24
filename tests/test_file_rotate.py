import uuid
import unittest
import os
from pylogger.logger_factory import LoggerFactory


class A:
    def __init__(self) -> None:
        LoggerFactory._maxBytes = 256
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self, param: str) -> None:
        self.logger.info(param)


class ContextLogTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = f"logs/{str(uuid.uuid4())}.log"
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        for file in os.listdir("logs"):
            if file.startswith(os.path.basename(self.textFilePath).split(".")[0]):
                os.remove(os.path.join("logs", file))

    def test_fileRotate(self) -> None:
        message = "A" * 32
        a = A()

        # 회전이 일어나도록 충분히 많은 메시지 기록
        for _ in range(5):
            a.do_something(message)

        # 로그 파일 리스트
        log_files = [
            file
            for file in os.listdir("logs")
            if file.startswith(os.path.basename(self.textFilePath).split(".")[0])
        ]

        # 회전된 로그 파일 확인
        self.assertTrue(len(log_files) > 1, "Log rotation did not occur as expected.")

        # 회전된 파일 중 일부 확인
        for log_file in log_files:
            file_path = os.path.join("logs", log_file)
            with open(file_path, "r") as f:
                content = f.read()
                self.assertIn(message, content, f"Expected message not found in {log_file}")


if __name__ == "__main__":
    unittest.main()
