import logging


class ConsoleLoggingHandler(logging.StreamHandler):
    def __init__(self, formatter: logging.Formatter, level: int = logging.DEBUG):
        super().__init__()
        self.setLevel(level)
        self.setFormatter(formatter)
