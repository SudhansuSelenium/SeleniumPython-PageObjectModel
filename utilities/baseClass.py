from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from resources.config import settings

class baseClass:
    instance = None

    @staticmethod
    def openPage(context):
        global driver
        global capabilities
        if settings['BrowserName'] == "Firefox":
            capabilities = DesiredCapabilities.FIREFOX
            capabilities['platform'] = settings['OS_Platform']
            capabilities['version'] = settings['BrowserVersion']
            capabilities['browserName']=settings['BrowserName']
            context.driver = webdriver.Remote(
                command_executor="https://sudhansusekhar2005:IlG2J1JGI8iCLgEriOA6ZDgnOJov7rHC47qeu5GGwpDTLd3eqG@hub.lambdatest.com/wd/hub",
                desired_capabilities=capabilities)
        context.driver.maximize_window()
        driver = context.driver

    @staticmethod
    def getDriver():
        return driver

    def get_deleteCookies(context):
        driver.delete_cookie()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = baseClass()
        return cls.instance

    @staticmethod
    def closePage(context):
        context.driver.quit()
        print "Quit Driver"


testBase = baseClass.get_instance()