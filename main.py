from logger_module import LoggerFactory


class A:
    def __init__(self):
        self.logger = LoggerFactory.getLogger(self.__class__.__name__)

    def do_something(self):
        self.logger.info("Doing something")


a = A()
a.do_something()
