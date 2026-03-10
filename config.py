import logging.handlers


# 使用日志的高级用法对于logging模块自带的root日志器进行配置的函数
def basic_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    # 5级别:DEBUG调试级别 INFO信息级别 WARNING警告级别 ERROR错误级别 CRITICAL致命错误
    logger.setLevel(level=logging.INFO)
    # 3.创建处理器-输出到日志文件
    lht = logging.handlers.TimedRotatingFileHandler("./log/tp_test.log", when='midnight',
                                                    interval=1, backupCount=2, encoding="utf8")
    # 4.创建处理器-输出到控制台
    ls = logging.StreamHandler()
    # 5.创建格式化器
    fomatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 6.给处理器添加格式化器
    lht.setFormatter(fomatter)
    ls.setFormatter(fomatter)
    # 7.给日至期添加处理器
    logger.addHandler(lht)
    logger.addHandler(ls)