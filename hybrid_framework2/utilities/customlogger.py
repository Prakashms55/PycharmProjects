import logging

class LogGen:
    @staticmethod
    def loggen():
        logger=logging.getLogger()
        fhandler=logging.FileHandler(filename='C:\Users\praka\PycharmProjects\hybrid_framework2\logs\automation.log',mode='a')
        formatter=logging.Formatter()
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
