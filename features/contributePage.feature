@contributePage
# Created by NIBEDITA SAHOO at 05-May-20
Feature: eGift - Contribute Page

  Scenario: verify labels in contribute page
    Given Contributor clicks on the Campaign contribute link with no contributor
    When Contributor lands on Campaign Contribute page
    Then Contributor sees Scholastic Logo displays
    And Contributor sees 'Contribute' button is displayed
    And Contributor sees 'Contribute' button is enabled
    And Contributor sees 'Campaign End Date' label is displayed
    And Contributor sees Teacher First name and Last name are displayed
@smoke
  Scenario: Verify contribute page when there is no contributor
    Given Contributor clicks on the Campaign contribute link with no contributor
    When Contributor lands on Campaign Contribute page
    Then Contributor sees Scholastic Logo displays
    And Contributor sees 'Contribute' button is displayed
    And Contributor sees 'Contribute' button is enabled
    And Contributor sees 0 of contributors contributed is displays
    And Contributor sees total amount of contributions contributed is displayed
    And Contributor sees goal amount is displays
    And Contributor sees campaign End date displays
    And Contributor sees Teacher First name and Last name are displayed
    And Contributor sees 'Confirm Payment' button is displayed
    And Contributors List section does not display
    And Contributor sees 'Contribute' button is displayed
    And Contributor sees 'Contribute' button is enabled


