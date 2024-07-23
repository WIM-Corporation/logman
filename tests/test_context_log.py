import uuid
import unittest
import os
from pylogger import LoggerFactory


class A:
    def __init__(self):
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self, param: str):
        self.logger.info(param)


class ContextLogTest(unittest.TestCase):
    def setUp(self):
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self):
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)
        LoggerFactory._initialized = False

    def test_contextLog(self):
        param1 = str(uuid.uuid4())
        param2 = str(uuid.uuid4())

        a = A()
        a.do_something(param1)
        a.do_something(param2)

        with open(self.textFilePath, "r") as f:
            lines = f.readlines()
            self.assertIn(param1, lines[0])
            self.assertIn(param2, lines[1])


if __name__ == "__main__":
    unittest.main()
