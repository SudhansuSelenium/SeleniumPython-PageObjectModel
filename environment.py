import sys
import time

from resources.config import getProperty
from utilities.baseClass import testBaseClass
from threading import Thread


def before_feature(context, feature):
    global featureTagValue
    for featureTagValue in feature.tags:
        pass
    print("Feature tag :",featureTagValue)

def before_scenario(context, scenario):
    if (featureTagValue == getProperty['tags'].replace("@","")) == True:
        print("Inside First test")
        testBaseClass.openPage()

    li = []
    for sctag in scenario.tags:
        li.append(sctag)
    print(li)

    if ('smoke' in li)==True:
         print("Inside 2nd test")
         testBaseClass.openPage()
         time.sleep(10)
    else:
        print("******** SKIPPING SCENARIO *******")
        scenario.skip()

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