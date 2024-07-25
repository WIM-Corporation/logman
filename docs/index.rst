.. logman documentation master file, created by
   sphinx-quickstart on Wed Jul 24 13:56:04 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Quickstart
==========

**logman** is inspired by the SLF4J LoggerFactory from the Spring ecosystem. It aims to provide a similar experience for Python developers, featuring JSON logging and log rotation capabilities.

1. Install logman:

   .. code-block:: bash

      $ pip install logman

2. Import and use the logger:

   .. code-block:: python
      :linenos:

      from logman import LoggerFactory

      class MyClass:
         def __init__(self):
            self.logger = LoggerFactory.getLogger(self.__class__.__name__)
         
         def my_method(self):
            self.logger.info('Hello, World!')

      myClass = MyClass()
      myClass.my_method()
   
   .. code-block:: bash

      $ python my_script.py
      {"context": "MyClass", "level": "INFO", "timestamp": "2024-07-24 16:25:10.016", "message": "Hello, World!", "thread": "MainThread"}

=====

Navigation
===========

.. toctree::
   :titlesonly:

   documentation/index
   recipes/index

.. toctree::
   :caption: Support
   :titlesonly:

   Github <https://github.com/WIM-Corporation/logman>
   Contact us <https://en.wimcorp.co.kr/>
