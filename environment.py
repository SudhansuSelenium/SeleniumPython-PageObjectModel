from behave_webdriver import driver

from resources.config import getProperty
from utilities.baseClass import testBaseClass
import allure
from allure_commons.types import AttachmentType

def before_feature(context, feature):
    global featureTagValue
    for featureTagValue in feature.tags:
        pass
    print("Feature tag :", featureTagValue)


def before_scenario(context, scenario):
    ############## scenario run with Feature tag ###################
    if (featureTagValue == getProperty['tags'].replace("@", "")) == True:
        print(scenario)
        testBaseClass.openPage(scenario)
    ############## scenario run with Scenario tag ###################
    if (featureTagValue != getProperty['tags'].replace("@", "")) == True:
        global scenarioTagList
        scenarioTagList = []
        for scenarioTag in scenario.tags:
            scenarioTagList.append(scenarioTag)
        if (getProperty['tags'].replace("@", "") in scenarioTagList) == True:
            print(scenario)
            testBaseClass.openPage(scenario)
        else:
            scenario.skip()

def after_scenario(context, scenario):
    try:
        if (featureTagValue == getProperty['tags'].replace("@", "")) == True or (
                getProperty['tags'].replace("@", "") in scenarioTagList) == True:
            print(scenario.status)
            if scenario.status == 'failed':
                with allure.step('open ya.ru and take screenshot'):
                    allure.attach('screenshot', testBaseClass.getDriver().get_screenshot_as_png(), type=AttachmentType.PNG)
                print("Scenario :", scenario.name, " failed")
                testBaseClass.getDriver().quit()
        testBaseClass.getDriver().quit()
    except(RuntimeError, TypeError, NameError):
        pass