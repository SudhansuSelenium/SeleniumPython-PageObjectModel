from behave import *

from pageobjects.contributePageObject import contributePageObject

contributePage = contributePageObject()
use_step_matcher("re")


@given("Contributor clicks on the Campaign contribute link with no contributor")
def step_impl(context):
    contributePage.launchCampaign(context, 'noContributorUrl')


@when("Contributor lands on Campaign Contribute page")
def step_impl(context):
    contributePage.verifyContributePageDisplayed()
    contributePage.verifyLabelsPresent()


@then("Contributor sees Scholastic Logo displays")
def step_impl(context):
    contributePage.verifyScholasticTopLogoDisplayed()


@step("Contributor sees 'Contribute' button is displayed")
def step_impl(context):
    contributePage.verifyContributeBtnDisplayed()


@step("Contributor sees 'Contribute' button is enabled")
def step_impl(context):
    contributePage.verifyContributeBtnDisplayed()


@step("Contributor sees 'Campaign End Date' label is displayed")
def step_impl(context):
    contributePage.verifyEndDateLabelDisplayed()


@step("Contributor sees Teacher First name and Last name are displayed")
def step_impl(context):
    contributePage.verifyTeacherFirstLastNameDisplayed()

### Scenario: Verify contribute page when there is no contributor

@step("Contributor sees 0 of contributors contributed is displays")
def step_impl(context):
    contributePage.verify0ContributorDisplayed()

@step("Contributor sees total amount of contributions contributed is displayed")
def step_impl(context):
    contributePage.verifyContributedAmount()


@step("Contributor sees goal amount is displays")
def step_impl(context):
    contributePage.verifyGoalAmtInContributePgDisplayed()



@step("Contributor sees campaign End date displays")
def step_impl(context):
    contributePage.verifyEndDateInContributePgDisplayed()


@step("Contributor sees 'Confirm Payment' button is displayed")
def step_impl(context):
    contributePage.verifyConfirmPaymentInContributePgDisplayed()

@step("Contributors List section does not display")
def step_impl(context):
    contributePage.verifyNoContributorsListMsg()
