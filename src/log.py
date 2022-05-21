import logging,os

class Log():
    def __init__(self) -> None:
        #解决windows系统在cmd运行日志显示异常问题
        os.system('')
        #设置日志输出样式
        logging.basicConfig(format = '\033[33m[%(asctime)s][%(levelname)s]:\033[0m%(message)s',level=logging.DEBUG)
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)
    
    def info(self,msg) -> None:
        logging.info(msg)

    def debug(self,msg) -> None:
        logging.debug(msg)

    def error(self,msg) -> None:
        logging.error(msg)
    
    def warning(self,msg) -> None:
        logging.warning(msg)

    def critical(self,msg) -> None:
        logging.critical(msg)
    