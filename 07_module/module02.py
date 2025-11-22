## logging 日志配置
import logging

logging.basicConfig(format='%(asctime)s-%(threadName)s-%(name)s-%(levelname)s-%(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.debug("debug 输出")
logger.info("info 输出")
logger.warning("warning 输出")
logger.error(" error 输出")

##format 格式
