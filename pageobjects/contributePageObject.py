from selenium.webdriver.common.by import By
from self import self

from resources.config import settings
from utilities.baseClass import baseClass, testBase

############################ Locators ###############################
contribute_Btn = "//a[@class='btn btn-primary'][contains(.,'Contribute')]"


class contributePageObject(baseClass):

    def __init__(self):
        testBase.openPage()

    def launchCampaign(self, contributePageUrl):
        if contributePageUrl == 'noContributorUrl':
            self.driver.get(settings['noContributorUrl'])
    ###############################################################
    # Scenario: verify labels in contribute page
    @staticmethod
    def verifyContributePageDisplayed():
        print("test")

    def verifyLabelsPresent(self):
        self.driver.find_element_by_xpath(contribute_Btn).click()


# EOS - Scenario: verify labels in contribute page


contributePage = contributePageObject()
