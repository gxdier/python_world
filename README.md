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


