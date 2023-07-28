import configparser

config=configparser.RawConfigParser()
config.read("C://Users//praka//PycharmProjects//behaveBDDframework//features//configuration//config.ini")
# print(config.sections())
# print(config.get('basic info','url'))
class Readconfig:

    @staticmethod
    def getapplicationurl():
        url=config.get('basic info','url')
        return url
    @staticmethod
    def launchbrowser():
        browser=config.get('basic info','browser')
        return browser