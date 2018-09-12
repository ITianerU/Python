import logging as log

#输出的日志格式
log_format = "%(asctime)s->%(levelname)s->%(message)s"

#配置日志
log.basicConfig(level=log.DEBUG,filename="log.txt",format=log_format)
log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")

log.log(log.DEBUG,"debug2")
log.log(log.INFO,"info2")
log.log(log.WARNING,"warning2")
log.log(log.ERROR,"error2")
log.log(log.CRITICAL,"critical2")