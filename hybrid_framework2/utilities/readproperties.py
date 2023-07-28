import configparser

config=configparser.RawConfigParser()
config.read("C:\Users\praka\PycharmProjects\hybrid_framework2\configuration\config.ini")

class readcongfig:
    @staticmethod
    def getappurl():
        url=config.get('common info','url')
        return url
    @staticmethod
    def getusername():
        username=config.get('coomon info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('coomon info', 'password')
        return password