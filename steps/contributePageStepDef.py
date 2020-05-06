from behave import *

from pageobjects.contributePageObject import contributePageObject, contributePage

use_step_matcher("re")


@given("Contributor clicks on the Campaign contribute link with no contributor")
def step_impl(context):
    contributePage.launchCampaign('noContributorUrl')


@when("Contributor lands on Campaign Contribute page")
def step_impl(context):
    contributePage.verifyContributePageDisplayed()
    contributePage.verifyLabelsPresent()



