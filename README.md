# Minipougne

## Original Package

This is some example code that is part of a [blog post on using GitHub (or other providers) as a PyPi Server](
https://medium.freecodecamp.org/how-to-use-github-as-a-pypi-server-1c3b0d07db2).

This repository defines a very simple package that just has a function that returns "world".

## Modification Logger

In the __ini__.py of the project

```
# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
print(__name__)
```

In the python_world.py

```
import logging

logging.debug('Debug mon minipougne)
logging.info('Info mon minipougne')
logging.warning('Warning mon minipougne)
logging.error('Error mon minipougne)
logging.critical('Critical mon minipougne)

```

## Calling this package's logger for our main applicaton

The logger is called python_world (`__name__`) so I thought something like that would work:
```
import logging
import sys

logger = logging.getLogger('python_world')
# logger = logging.getLogger() # but then it is the ROOT logger (?)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
file_handler = logging.StreamHandler(sys.stdout)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
```


