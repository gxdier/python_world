# Minipougne

## Modification Logger

As suggested by https://docs.python-guide.org/writing/logging/#logging-in-a-library, in the `__ini__.py` of the project

```
# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
print(__name__)
```

In the `world.py`

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

import python_world

import logging
import sys

logger = logging.getLogger('python_world')
# logger = logging.getLogger() # but then it is the ROOT logger (?)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
file_handler = logging.StreamHandler(sys.stdout)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

python_world.world.world()

```


## Logging: how to ?
in your package:
```python
import logging
logger = logging.getLogger(__name__)  # creates a logger named __name__ (let's call it "package_name")
# then set a null handler on logger
# log what you want using this logger: logger.info("toto")
```

Then, in your application:
get your package's logger :
```python
import logging
logger_package = logging.getLogger("package_name")
# set the desired handler on logger_package
# your package will now log stuff using your handler 
```

Howerver, if you do in your package 
```python
import logging
logging.info("toto")
```
then "toto" will be logged by the `root` logger, even if you call it from your application.