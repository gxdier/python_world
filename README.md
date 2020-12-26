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


