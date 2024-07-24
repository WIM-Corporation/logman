# mypy: ignore-errors

import logging


class CustomLogger(logging.Logger):
    def error(self, msg, *args, **kwargs) -> None:
        if "exc_info" not in kwargs:
            kwargs["exc_info"] = True
        super().error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs) -> None:
        if "exc_info" not in kwargs:
            kwargs["exc_info"] = True
        super().critical(msg, *args, **kwargs)

    def fatal(self, msg, *args, **kwargs) -> None:
        if "exc_info" not in kwargs:
            kwargs["exc_info"] = True
        super().fatal(msg, *args, **kwargs)
