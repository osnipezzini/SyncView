import logging
import os
from logging.handlers import TimedRotatingFileHandler


def init_logger(logfile) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.handlers = []
    handler = TimedRotatingFileHandler(
        filename=logfile, when='midnight', backupCount=30)
    logger.addHandler(handler)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s  %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    if os.environ.get('ELOGLEVEL'):
        level = os.environ.get('ELOGLEVEL')
        if level == 'debug':
            logger.setLevel(logging.DEBUG)
        elif level == 'error':
            logger.setLevel(logging.ERROR)
        elif level == 'warning':
            logger.setLevel(logging.WARNING)
        elif level == 'critical':
            logger.setLevel(logging.CRITICAL)
        else:
            logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.INFO)

    return logger

