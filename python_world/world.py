import logging


def world():
    logger = logging.getLogger(__name__)
    logger.debug('Debug mon minipougne')
    logger.info('Info mon minipougne')
    logger.warning('Warning mon minipougne')
    logger.error('Error mon minipougne')
    logger.critical('Critical mon minipougne')
    return "world"
