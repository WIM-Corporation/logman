import unittest
import os
import uuid

from logman.logger_factory import LoggerFactory
from logman.handler import FileRotateLoggingHandler, ConsoleLoggingHandler


class ListHandlersTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)

    def test_listHandlers_initial(self) -> None:
        handlers = LoggerFactory.listHandlers()
        self.assertEqual(len(handlers), 2)
        self.assertIsInstance(handlers[0], FileRotateLoggingHandler)
        self.assertIsInstance(handlers[1], ConsoleLoggingHandler)


if __name__ == "__main__":
    unittest.main()
