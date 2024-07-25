import unittest
import uuid
import os

from unittest.mock import MagicMock, patch
from logman.logger_factory import LoggerFactory
from logman.handler import FileRotateLoggingHandler, ConsoleLoggingHandler


class AddHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)

    @patch("logman.handler.FileRotateLoggingHandler")
    def test_addHandler(self, MockFileRotateLoggingHandler: MagicMock) -> None:
        handlers = LoggerFactory.listHandlers()
        self.assertEqual(len(handlers), 2)
        self.assertIsInstance(handlers[0], FileRotateLoggingHandler)
        self.assertIsInstance(handlers[1], ConsoleLoggingHandler)

        mock_handler = MockFileRotateLoggingHandler()
        LoggerFactory.addHandler(mock_handler)
        handlers = LoggerFactory.listHandlers()
        self.assertEqual(len(handlers), 3)
        self.assertIn(mock_handler, handlers)


if __name__ == "__main__":
    unittest.main()
