from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from resources.config import desired_capabilities


class testBaseClass:

    @staticmethod
    def openPage():
        global driver
        global capabilities
        if desired_capabilities['remoteDriver'] == "True":
            if desired_capabilities['BrowserName'] == "Firefox":
                capabilities = DesiredCapabilities.FIREFOX
            elif desired_capabilities['BrowserName'] == "Chrome":
                capabilities = DesiredCapabilities.CHROME
            elif desired_capabilities['BrowserName'] == "IE":
                capabilities = DesiredCapabilities.INTERNETEXPLORER
            elif desired_capabilities['Edge'] == "Edge":
                capabilities = DesiredCapabilities.EDGE
            elif desired_capabilities['Safari'] == "Safari":
                 capabilities = DesiredCapabilities.SAFARI
            capabilities['platform'] = desired_capabilities['OS_Platform']
            capabilities['version'] = desired_capabilities['BrowserVersion']
            capabilities['browserName'] = desired_capabilities['BrowserName']
            #capabilities['name'] = scenario.name
            capabilities['build'] = "eGift Testing Python"
            driver = webdriver.Remote(
                command_executor=desired_capabilities["lambdaTest"],desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(executable_path="D:\\PythonProjects\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()

    @staticmethod
    def getDriver():
        return driver

    @staticmethod
    def deleteCookies():
        driver.delete_all_cookies()

    @staticmethod
    def closePage():
        driver.quit()

testBase = testBaseClass()