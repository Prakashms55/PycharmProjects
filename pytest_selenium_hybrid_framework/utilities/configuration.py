import configparser

config=configparser.RawConfigParser()
config.read("configuration/config.ini")

class ReadConfig:

    @staticmethod
    def getapplurl():
        url=config.get("basic info","url")
        return url

    @staticmethod
    def launch_browser():
        browser=config.get("basic info","browser")
        return browser