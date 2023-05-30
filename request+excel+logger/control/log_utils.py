import logging
import logging.config

my_log = logging.config.fileConfig('./config/log.ini')
logger = logging.getLogger('root')

'''
其他模块中引用

from log import logger

logger.info('asd')
logger.error('asd)

'''
