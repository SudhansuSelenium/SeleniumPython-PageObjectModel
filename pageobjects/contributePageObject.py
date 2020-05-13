import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

from resources.config import settings
from utilities.baseClass import baseClass, testBase

############################ Locators ###############################
contributePg_btn = "//a[@class='btn btn-primary'][contains(.,'Contribute')]"
contributePg_Title = "//h1[contains(text(),'CampaignAutoTest')]"
scholasticTop_Logo = "//img[@alt='Scholastic']"
contributePg_EndDateLabel = "//span[@class='label-campaign-goal'][contains(.,'Campaign End Date')]"
contributePg_TeacherName = "//div[@class='col teacher-campaign-goal']"
contributePg_TotalContributor = ".//a[@href='#sec-contributors']"


class contributePageObject(baseClass):



    @staticmethod
    def launchCampaign(context, contributePageUrl):
        if contributePageUrl == 'noContributorUrl':
            baseClass.getDriver().get(settings['noContributorUrl'])

    ###############################################################
    # Scenario: verify labels in contribute page

    @staticmethod
    def verifyContributePageDisplayed():
        time.sleep(5)
        global teacherFirstLastName
        global teacherFirstLastName
        WebDriverWait(baseClass.getDriver(), 10).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, contributePg_Title)))
        assert baseClass.getDriver().find_element_by_xpath(contributePg_Title).text == settings['contributePg_Title']
        teacherFirstLastName = baseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        teacherFirstLastName = baseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        totalContributor = baseClass.getDriver().find_element_by_xpath(contributePg_TotalContributor).text.strip()
        print totalContributor

    @staticmethod
    def verifyLabelsPresent():
        if baseClass.getDriver().find_element_by_xpath(contributePg_btn).is_displayed():
            assert baseClass.getDriver().find_element_by_xpath(contributePg_btn).is_enabled()

    @staticmethod
    def verifyScholasticTopLogoDisplayed():
        WebDriverWait(baseClass.getDriver(), 20).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, scholasticTop_Logo)))
        assert baseClass.getDriver().find_element_by_xpath(scholasticTop_Logo).is_displayed()

    @staticmethod
    def verifyContributeBtnDisplayed():
        assert baseClass.getDriver().find_element_by_xpath(contributePg_btn).is_displayed()
        assert baseClass.getDriver().find_element_by_xpath(contributePg_btn).is_enabled()

    @staticmethod
    def verifyEndDateLabelDisplayed():
        assert baseClass.getDriver().find_element_by_xpath(contributePg_EndDateLabel).is_displayed()

    @staticmethod
    def verifyTeacherFirstLastNameDisplayed():
        teacherFN = teacherFirstLastName.split()
        assert teacherFN[1] == settings['contributePg_TeacherFirstName']

    @staticmethod
    def verifyTeacherLastNameDisplayed():
        teacherLN = teacherFirstLastName.split()
        assert teacherLN[2] == settings['contributePg_TeacherLastName']

# EOS - Scenario: verify labels in contribute page
### Scenario: Verify contribute page when there is no contributor
    @staticmethod
    def verifyTeacherLastNameDisplayed1():
        print 'test2'

### EOS - Scenario: Verify contribute page when there is no contributor