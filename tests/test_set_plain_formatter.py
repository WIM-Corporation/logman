import uuid
import unittest
import os

from logman.logger_factory import LoggerFactory
from logman.formatter import PlainFormatter


class SetPlainFormatterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath
        LoggerFactory.setFormatter(PlainFormatter())
        self.logger = LoggerFactory.getLogger("PlainFormatterTest")

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)

    def test_plain_formatter_info_log(self) -> None:
        with self.assertLogs("PlainFormatterTest", level="INFO") as cm:
            self.logger.info("This is an info message")
        log_output = cm.output[0]
        self.assertEqual(log_output, "INFO:PlainFormatterTest:This is an info message")

    def test_plain_formatter_error_log(self) -> None:
        try:
            1 / 0
        except ZeroDivisionError:
            with self.assertLogs("PlainFormatterTest", level="ERROR") as cm:
                self.logger.error("This is an error message")

        log_output = cm.output[0]
        self.assertIn("ERROR:PlainFormatterTest:This is an error message", log_output)


if __name__ == "__main__":
    unittest.main()
