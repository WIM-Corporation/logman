import uuid
import unittest
import os
from pylogger import LoggerFactory


class A:
    def __init__(self):
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self):
        self.logger.info(uuid.uuid4())


class DuplicateContextCacheTest(unittest.TestCase):
    def setUp(self):
        self.textFilePath = os.path.join("logs", f"{str(uuid.uuid4())}.log")
        LoggerFactory._filePath = self.textFilePath

    def tearDown(self):
        if os.path.exists(self.textFilePath):
            os.remove(self.textFilePath)
        LoggerFactory._initialized = False

    def test_duplicateContextCache(self):
        a1 = A()
        a2 = A()

        a1.do_something()
        a2.do_something()

        self.assertNotEqual(a1, a2)
        self.assertEqual(a1.logger, a2.logger)


if __name__ == "__main__":
    unittest.main()
