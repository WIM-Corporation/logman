*****************
Handler
*****************

Adding and Removing Handlers
=============================

In `logman`, you can add or remove handlers from the root logger using the `LoggerFactory` class. This allows you to customize the logging behavior by adding handlers that write logs to different destinations or format them differently.

Adding a Handler
-----------------

To add a handler, use the `addHandler` method of `LoggerFactory`. Here is an example of how to add a `FileRotateLoggingHandler`:

.. code-block:: python

    from logman.logger_factory import LoggerFactory
    from logman.handler import FileRotateLoggingHandler
    from logman.formatter import JsonFormatter

    # Create a new handler
    json_formatter = JsonFormatter()
    rotate_handler = FileRotateLoggingHandler(level=logging.INFO, formatter=json_formatter, maxBytes=1024 * 1024 * 10, filePath='logs/app.log')

    # Add the handler
    LoggerFactory.addHandler(rotate_handler)

Removing a Handler
-------------------

To remove a handler, use the `removeHandler` method of `LoggerFactory`. Here is an example of how to remove the `FileRotateLoggingHandler` we added earlier:

.. code-block:: python

    from logman.logger_factory import LoggerFactory

    # Remove the handler
    LoggerFactory.removeHandler(rotate_handler)

Listing Handlers
----------------

You can list the current handlers attached to the root logger using the `listHandlers` method of `LoggerFactory`:

.. code-block:: python

    from logman.logger_factory import LoggerFactory

    # List the handlers
    handlers = LoggerFactory.listHandlers()
    for handler in handlers:
        print(handler)


Using Custom Handlers
======================

You can create custom handlers by inheriting from more specific `logging` handler base classes to fit your specific logging needs. Below are examples of how to implement and use custom handlers in your logging setup.

Custom File Handler
-------------------

A custom logging handler that writes logs to a file with rotation. This example uses `RotatingFileHandler`.

.. code-block:: python

    import logging

    class CustomFileHandler(logging.handlers.RotatingFileHandler):
        def __init__(self, filename, maxBytes=0, backupCount=0, encoding=None, level = logging.DEBUG):
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            super().__init__(filename, maxBytes=maxBytes, backupCount=backupCount, encoding=encoding)
            self.setLevel(level)

Custom Console Handler
-----------------------

A custom logging handler that outputs logs to the console, inheriting from `StreamHandler`.

.. code-block:: python

    import logging

    class CustomConsoleHandler(logging.StreamHandler):
        def __init__(self, level: int = logging.DEBUG):
            super().__init__()
            self.setLevel(level)

Example of Using Custom Handlers
---------------------------------

Here's an example of how to use the custom handlers in your logging setup.

.. code-block:: python

    from logman import LoggerFactory
    from logman.formatter import JsonFormatter

    # Create and add custom handlers
    json_formatter = JsonFormatter()

    file_handler = CustomFileHandler('logs/app.log', maxBytes=1024*1024*5, backupCount=5)
    file_handler.setFormatter(json_formatter)

    console_handler = CustomConsoleHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    LoggerFactory.addHandler(file_handler)
    LoggerFactory.addHandler(console_handler)

    # Get a logger and log a message
    logger = LoggerFactory.getLogger('CustomLoggerExample')
    logger.info('This is an info message')

By following these instructions, you can effectively customize and extend the logging capabilities of your Python application using `logman` and leveraging the specific `logging` handler base classes.
