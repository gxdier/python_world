from python_world import world
import logging
import sys

# Here we get the logger of python_world 
logger = logging.getLogger('python_world')
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")
file_handler = logging.StreamHandelr(sys.stdout)
file_handler = setFormatter(formatter)
logger.addHandler(file_handler)

world.world()
