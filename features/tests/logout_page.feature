# Created by elena.kuletsky at 5/4/2024
Feature: Logout Tests

  @smoke
  Scenario: Logout Test: Ensure users can log out of their accounts without any errors.
    Given Login
    When Tap on the Avatar in the top-left corner
    And Tap on ‘Settings’ from side menu
    And Tap on ‘Logout’ button
    And Confirm logout, tap on Yes
    Then Verify that user logged out

