import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from self import self

from resources.config import settings
from utilities.baseClass import baseClass, testBase

############################ Locators ###############################
contribute_Btn = "//a[@class='btn btn-primary'][contains(.,'Contribute')]"
contributePg_Title = "//h1[contains(text(),'CampaignAutoTest')]"


class contributePageObject(baseClass):

    def __init__(self):
        testBase.openPage()

    @staticmethod
    def launchCampaign(contributePageUrl):
        if contributePageUrl == 'noContributorUrl':
            testBase.driver.get(settings['noContributorUrl'])
    ###############################################################
    # Scenario: verify labels in contribute page

    @staticmethod
    def verifyContributePageDisplayed():
        WebDriverWait(testBase.driver, 20).until(ExpectedConditions.visibility_of_element_located((By.XPATH, contributePg_Title)))
        assert testBase.driver.find_element_by_xpath(contributePg_Title).is_displayed()
        print(settings['contributePg_Title'])
        assert testBase.driver.find_element_by_xpath(contributePg_Title).text == settings['contributePg_Title']

    @staticmethod
    def verifyLabelsPresent():
        if testBase.driver.find_element_by_xpath(contribute_Btn).is_displayed():
            assert testBase.driver.find_element_by_xpath(contribute_Btn).is_enabled()
        testBase.driver.find_element_by_xpath(contribute_Btn).click()


# EOS - Scenario: verify labels in contribute page


contributePage = contributePageObject()
