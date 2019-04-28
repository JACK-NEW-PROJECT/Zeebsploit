import logging
from colorlog import ColoredFormatter

def logger(name):
    format_ = ColoredFormatter(
        '%(log_color)s%(levelname)s%(reset)s %(message)s',
        log_colors={
            '[+]':'blue',
            '[!]':'yellow',
            '[-]':'red',
            '[x]':'red_bold',
            '[*]':'green'
        }
    )
    logging.addLevelName(10,'[+]')
    logging.addLevelName(20,'[!]')
    logging.addLevelName(30,'[-]')
    logging.addLevelName(40,'[x]')
    logging.addLevelName(50,'[*]')
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(format_)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


