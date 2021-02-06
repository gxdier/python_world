from python_world import world
from python_world import world1
import logging
import sys

# Here we get the logger of python_world 
logger = logging.getLogger('python_world')
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")
file_handler = logging.StreamHandler(sys.stdout)
file_handler = setFormatter(formatter)
logger.addHandler(file_handler)

# Si je fais ca alors le niveau est bien set a INFO et ca me print bien les log bien formatte dans la stdout MAIS
# ca print aussi les log non formatter dans la stderr

# Si je mets pas le bloc de code ci-dessus alors ca me print juste a partir du niveau WARNING dans la stderr (alors que
# ca ne dervait rien printer)

world.world()

world1.world()
