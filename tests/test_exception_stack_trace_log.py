import uuid
import unittest
import os
import json

from pylogger.logger_factory import LoggerFactory


class A:
    def __init__(self) -> None:
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self) -> None:
        try:
            1 / 0
        except ZeroDivisionError:
            self.logger.error("ZeroDivisionError Error occurred")


class ExceptionStackTraceLogTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)

    def test_exceptionStackTraceLog(self) -> None:
        a = A()
        a.do_something()

        with open(self.textFilePath, "r") as f:
            lines = f.readlines()
            jsonLog = json.loads(lines[0])
            self.assertEqual(jsonLog["context"], "A")
            self.assertEqual(jsonLog["level"], "ERROR")
            self.assertEqual(jsonLog["message"], "ZeroDivisionError Error occurred")
            self.assertIn("stack_trace", jsonLog)


if __name__ == "__main__":
    unittest.main()
