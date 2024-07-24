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
            time.sleep(1)


if __name__ == "__main__":
    foo = Foo()
    bar = Bar()

    # Create threads for Foo and Bar logging
    foo_thread = threading.Thread(target=foo.logRandomNumber)
    bar_thread = threading.Thread(target=bar.logRandomNumber)

    # Start the threads
    foo_thread.start()
    bar_thread.start()

    # Join the threads to the main thread to keep them running
    foo_thread.join()
    bar_thread.join()
