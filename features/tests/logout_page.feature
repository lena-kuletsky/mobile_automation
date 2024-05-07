# Created by elena.kuletsky at 5/4/2024
Feature: Logout Tests

  @smoke
  Scenario: Logout Test: Ensure users can log out of their accounts without any errors.
    Given Open the app
    When Tap on the Avatar in the top-left corner
    And Tap on ‘Settings’ from side menu
    And Tap on ‘Logout’ button
    And Tap on ‘Yes’, answering the question ‘Are you sure you want to logout?’
    Then Verify that user logged out successfully