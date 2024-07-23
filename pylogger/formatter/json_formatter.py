import logging
import time
import json


class JsonFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        if datefmt:
            return super().formatTime(record, datefmt)
        ct = self.converter(record.created)
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
        return s

    def formatException(self, ei):
        return super().formatException(ei)

    def format(self, record):
        if hasattr(record, "formatted_message"):
            return record.formatted_message

        log_record = {
            "context": record.name,
            "level": record.levelname,
            "timestamp": self.formatTime(record, self.datefmt),
            "message": record.getMessage(),
            "thread": record.threadName,
        }

        if record.exc_info:
            log_record["stack_trace"] = self.formatException(record.exc_info)

        if record.stack_info:
            log_record["stack_info"] = record.stack_info

        record.formatted_message = json.dumps(log_record, ensure_ascii=False)
        return record.formatted_message
