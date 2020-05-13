
from utilities.baseClass import baseClass


def before_scenario(context, scenario):
    print scenario
    baseClass.openPage(context)


def after_scenario(context, scenario):
    if  scenario.status == 'failed':
        print "faoiled"
        context.driver.save_screenshot("E:\\screenshot\\failed.png")
    else:
        print "passed"
    baseClass.closePage(context)