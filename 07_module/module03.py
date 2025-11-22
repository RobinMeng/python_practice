## logging 日志配置
import logging

## 日志输出handler
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', level=logging.DEBUG,
                    handlers=[std_handler, file_handler])

logger = logging.getLogger(__name__)

logger.debug("debug 输出")
logger.info("info 输出")
logger.warning("warning 输出")
logger.error(" error 输出")
