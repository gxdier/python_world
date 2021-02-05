from python_world import world
import logging

world.world()
logger = logging.getLogger("python_world")
logger.warning("toto")
logger.addHandler(logging.StreamHandler())
logger.warning("PUTE")