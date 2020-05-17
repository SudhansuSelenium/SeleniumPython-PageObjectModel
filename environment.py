import sys
import time

from resources.config import getProperty
from utilities.baseClass import testBaseClass
from threading import Thread


def before_feature(context, feature):
    global featureTag
    featureTag = feature.tags


def before_scenario(context, scenario):
    global scenarioTagslist

    # global scenarioTagValue
    # scenarioTagValue = scenario.tags
    #################################################################################
    #########################Scenarios having no tags################################
    # if featureTag:
    #     print("%%%%%%%%%%%%%%%%%%%%%%%%%,", scenario.tags)
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^,",getProperty['tags'])
    #     if scenario.tags == []:
    #         print(scenario)
    #         testBaseClass.openPage()
    ##################################################################################
    ###################Scenario having same/different/multiple tags###################
    if featureTag:
        scenarioTagslist = []
        for scenarioTagValue in scenario.tags:
            scenarioTagslist.append(scenarioTagValue)
        # if getProperty['tags'].replace("@", "") in scenarioTagslist:
        #     testBaseClass.openPage()
        #     print(
        #         "---------------------------------------OPEN PAGE with tags----------------------------------------------------------")
        ############################Scenarios will run with No tags##########################
        print("Conditions1 :",getProperty['tags'] == "[]" and scenario.tags == [])
        if (getProperty['tags'] == "[]" and scenario.tags == []) ==True :
            testBaseClass.openPage()
            print(
                "---------------------------------------OPEN PAGE NO TAGS----------------------------------------------------------")
        ############################Scenarios with No tags##########################
        ############################Scenarios will run with tags#############################
        print("Conditions2 :",getProperty['tags'].replace("@", "") in scenarioTagslist)
        if (getProperty['tags'].replace("@", "") in scenarioTagslist)== True:
            testBaseClass.openPage()
            print(
                "---------------------------------------OPEN PAGE NO TAGS----------------------------------------------------------")
        else:
            scenario.skip()
            print(
                "-------------------------------------SKIP------------------------------------------------------------")



    #################################################################################

# def after_scenario(context, scenario):
#     try:
#         if getProperty['tags'] == "{}{}".format("@", scenarioTagValue):
#             if scenario.status == 'failed':
#                 context.driver.save_screenshot("E:\\screenshot\\failed.png")
#                 print("Scenario :", scenario.name, " failed")
#             else:
#                 testBaseClass.closePage()
#     except(RuntimeError, TypeError, NameError):
#         pass