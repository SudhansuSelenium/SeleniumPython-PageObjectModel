import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from resources.config import getProperty
from utilities.baseClass import testBaseClass, testBase

############################ Locators ###############################
contributePg_btn = "//a[@class='btn btn-primary'][contains(.,'Contribute')]"
contributePg_Title = "//h1[contains(text(),'CampaignAutoTest')]"
scholasticTop_Logo = "//img[@alt='Scholastic']"
contributePg_EndDateLabel = "//span[@class='label-campaign-goal'][contains(.,'Campaign End Date')]"
contributePg_TeacherName = "//div[@class='col teacher-campaign-goal']"
contributePg_TotalContributor = ".//a[@href='#sec-contributors']"


class contributePageObject(testBaseClass):

    @staticmethod
    def launchCampaign(context, contributePageUrl):
        if contributePageUrl == 'noContributorUrl':
            testBaseClass.getDriver().get(getProperty['noContributorUrl'])

    ###############################################################
    # Scenario: verify labels in contribute page
    @staticmethod
    def verifyContributePageDisplayed():
        time.sleep(5)
        global teacherFirstLastName
        global teacherFirstLastName
        WebDriverWait(testBaseClass.getDriver(), 10).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, contributePg_Title)))
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_Title).text == getProperty['contributePg_Title']
        teacherFirstLastName = testBaseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        teacherFirstLastName = testBaseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        totalContributor = testBaseClass.getDriver().find_element_by_xpath(contributePg_TotalContributor).text.strip()

    @staticmethod
    def verifyLabelsPresent():
        if testBaseClass.getDriver().find_element_by_xpath(contributePg_btn).is_displayed():
            assert testBaseClass.getDriver().find_element_by_xpath(contributePg_btn).is_enabled()

    @staticmethod
    def verifyScholasticTopLogoDisplayed():
        WebDriverWait(testBaseClass.getDriver(), 20).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, scholasticTop_Logo)))
        assert testBaseClass.getDriver().find_element_by_xpath(scholasticTop_Logo).is_displayed()

    @staticmethod
    def verifyContributeBtnDisplayed():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_btn).is_displayed()
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_btn).is_enabled()

    @staticmethod
    def verifyEndDateLabelDisplayed():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_EndDateLabel).is_displayed()

    @staticmethod
    def verifyTeacherFirstLastNameDisplayed():
        teacherFN = teacherFirstLastName.split()
        assert teacherFN[1] == getProperty['contributePg_TeacherFirstName']

    @staticmethod
    def verifyTeacherLastNameDisplayed():
        teacherLN = teacherFirstLastName.split()
        assert teacherLN[2] == getProperty['contributePg_TeacherLastName']

# EOS - Scenario: verify labels in contribute page
### Scenario: Verify contribute page when there is no contributor
    @staticmethod
    def verifyTeacherLastNameDisplayed1():
        print ('test2')

    @staticmethod
    def verifyTeacherLastNameDisplayed2():
        print('test4')
### EOS - Scenario: Verify contribute page when there is no contributor