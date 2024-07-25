*****************
Formatter
*****************

Using Custom Formatters
========================

You can create custom formatters by inheriting from `logging.Formatter` to fit your specific logging needs. Below is an example of how to implement and use custom formatters in your logging setup.

Creating a Custom Formatter
----------------------------

Here is an example of a custom formatter that outputs log records with specific fields in a custom format.

.. code-block:: python

    import logging
    import time
    from typing import Optional, Any

    class CustomFormatter(logging.Formatter):
        def formatTime(self, record: logging.LogRecord, datefmt: Optional[str] = None) -> str:
            if datefmt:
                return super().formatTime(record, datefmt)
            ct = self.converter(record.created)
            t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = "%s.%03d" % (t, record.msecs)
            return s

        def format(self, record: Any) -> str:
            formatted_message = f"{self.formatTime(record)} - {record.levelname} - {record.name} - {record.getMessage()}"

            if record.exc_info:
                formatted_message += f"\n{self.formatException(record.exc_info)}"

            if record.stack_info:
                formatted_message += f"\n{record.stack_info}"

            return formatted_message


Applying the Custom Formatter
------------------------------

Once you have created a custom formatter, you can apply it to all handlers in your logging setup using `LoggerFactory`. Here is how you can do it:

.. code-block:: python

    from logman import LoggerFactory
    from custom_formatter import CustomFormatter

    # Create an instance of your custom formatter
    custom_formatter = CustomFormatter()

    # Apply the custom formatter to all handlers
    LoggerFactory.setFormatter(custom_formatter)

By following these steps, you can implement and use custom formatters in your Python logging setup effectively.
