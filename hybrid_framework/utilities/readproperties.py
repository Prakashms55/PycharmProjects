import configparser

config=configparser.RawConfigParser()
config.read("C://Users//praka//PycharmProjects//hybrid_framework//configuration//config.ini")
# print(config.sections())
# print(config.get('common info','base_url'))
class Readconfig:

    @staticmethod
    def getapplicationurl():
        url=config.get('common info','base_url')
        return url
    @staticmethod
    def getuseremail():
        email=config.get('common info','email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password