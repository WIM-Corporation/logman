import uuid
import unittest
import os
from pylogger.logger_factory import LoggerFactory


class A:
    def __init__(self) -> None:
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self, param: str) -> None:
        self.logger.info(param)


class DuplicateContextCacheTest(unittest.TestCase):
    def setUp(self) -> None:
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self) -> None:
        LoggerFactory._initialized = False
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)

    def test_duplicateContextCache(self) -> None:
        a1 = A()
        a2 = A()

        a1.do_something(str(uuid.uuid4()))
        a2.do_something(str(uuid.uuid4()))

        self.assertNotEqual(a1, a2)
        self.assertEqual(a1.logger, a2.logger)


if __name__ == "__main__":
    unittest.main()
