import random
import time
import threading
from logman import LoggerFactory


class Foo:
    def __init__(self) -> None:
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def logRandomNumber(self) -> None:
        while True:
            self.logger.info(f"Generated random number: {random.randint(1, 10000)}")
            time.sleep(1)


class Bar:
    def __init__(self) -> None:
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def logRandomNumber(self) -> None:
        while True:
            self.logger.info(f"Generated random number: {random.randint(1, 10000)}")
            time.sleep(15)


class Baz:
    def __init__(self) -> None:
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def logRandomNumber(self) -> None:
        while True:
            self.logger.error(f"Generated random number: {random.randint(1, 10000)}")
            time.sleep(30)


if __name__ == "__main__":
    foo = Foo()
    bar = Bar()
    baz = Baz()

    # Create threads for Foo and Bar logging
    # foo_thread = threading.Thread(target=foo.logRandomNumber)
    bar_thread = threading.Thread(target=bar.logRandomNumber)
    baz_thread = threading.Thread(target=baz.logRandomNumber)

    # Start the threads
    # foo_thread.start()
    bar_thread.start()
    baz_thread.start()

    # Join the threads to the main thread to keep them running
    # foo_thread.join()
    bar_thread.join()
    baz_thread.join()
