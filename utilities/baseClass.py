import self
from selenium import webdriver
from resources.config import settings


class baseClass:

    instance = None

    def __init__(self):
        print(settings['browser'])
        if settings['browser'] == 'chrome':
            self.driver = webdriver.Chrome(executable_path="D:\\PythonProjects\\chromedriver_win32\\chromedriver.exe")
        elif settings['browser'] == 'firefox':
            self.driver = webdriver.Firefox(executable_path="D:\\PythonProjects\\chromedriver_win32\\chromedriver.exe")
        else:
            print("No browser mentioned")

    def openPage(self):
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def get_deleteCookies(self):
        self.driver.delete_cookie()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = baseClass()
        return cls.instance


testBase = baseClass.get_instance()
