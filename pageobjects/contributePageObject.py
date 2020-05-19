import time
import unittest

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
contributePg_TotalContributionAmt = "//div[@class='col text-left'][contains(.,'$')]"
contributePg_TotalGoalAmt = "//div[@class='col text-right'][contains(.,'$')]"
contributePg_EndCampDate ="//div[contains(@class,'col date-campaign-goal')]"
contributePg_ConfirmPaymentBtn = "//button[@type='submit'][contains(.,'confirm payment')]"
contributePg_NoContributeMsg = "//p[contains(.,'You don’t have any contributors yet.')]"


class contributePageObject(testBaseClass, unittest.TestCase):

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
        global totalContributor
        global totalContributionAmt
        global totalGoalAmtTxt
        global campaignEndDate
        global noContributorListMsg
        WebDriverWait(testBaseClass.getDriver(), 10).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, contributePg_Title)))
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_Title).text == getProperty[
            'contributePg_Title']
        teacherFirstLastName = testBaseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        teacherFirstLastName = testBaseClass.getDriver().find_element_by_xpath(contributePg_TeacherName).text.strip()
        totalContributor = testBaseClass.getDriver().find_element_by_xpath(contributePg_TotalContributor).text.strip()
        totalContributionAmt = testBaseClass.getDriver().find_element_by_xpath(contributePg_TotalContributionAmt).text
        totalGoalAmtTxt = testBaseClass.getDriver().find_element_by_xpath(contributePg_TotalGoalAmt).text
        campaignEndDate = testBaseClass.getDriver().find_element_by_xpath(contributePg_EndCampDate).text
        noContributorListMsg = testBaseClass.getDriver().find_element_by_xpath(contributePg_NoContributeMsg).text

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


    def verifyEndDateLabelDisplayed(self):
        self.assertTrue(testBaseClass.getDriver().find_element_by_xpath(contributePg_EndDateLabel).is_displayed())


    def verifyTeacherFirstLastNameDisplayed(self):
        teacherFN = teacherFirstLastName.split()
        self.assertEqual(teacherFN[1],getProperty['contributePg_TeacherFirstName'])


    def verifyTeacherLastNameDisplayed(self):
        teacherLN = teacherFirstLastName.split()
        self.assertEqual(teacherLN[2],getProperty['contributePg_TeacherLastName'])

    # EOS - Scenario: verify labels in contribute page
    ### Scenario: Verify contribute page when there is no contributor

    def verify0ContributorDisplayed(self):
        if totalContributor[0] == 0:
            self.assertEqual(totalContributor[1], 'contributors')

    @staticmethod
    def verifyContributedAmount():
        if int(totalContributor[0]) == 0:
            assert int(totalContributionAmt[1]) == 0
            assert totalContributionAmt[0] == "$"
        elif int(totalContributor[0]) > 0:
            assert int(totalContributionAmt[1]) > 0
            assert totalContributionAmt[0] == "$"

    @staticmethod
    def verifyGoalAmtInContributePgDisplayed():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_TotalGoalAmt).is_displayed()

    @staticmethod
    def verifyEndDateInContributePgDisplayed():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_EndCampDate).is_displayed()

    @staticmethod
    def verifyConfirmPaymentInContributePgDisplayed():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_ConfirmPaymentBtn).is_displayed()
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_ConfirmPaymentBtn).is_enabled()

    @staticmethod
    def verifyNoContributorsListMsg():
        assert testBaseClass.getDriver().find_element_by_xpath(contributePg_NoContributeMsg).is_displayed()
        assert noContributorListMsg == getProperty['noContributorListMessage']

### EOS - Scenario: Verify contribute page when there is no contributor