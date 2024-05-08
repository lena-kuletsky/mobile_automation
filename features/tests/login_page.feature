# Created by elena.kuletsky at 5/4/2024
Feature: Login Tests

  @smoke
  Scenario: Login Test: Verify that the user can log in successfully with valid credentials.
#    Given Open the app
#    When Tap on Allow button
#    When Tap on ‘Get Started’ button below
#    And Enter valid phone number
#    And Tap on 'Next'
#    And Enter the verification code that was received
#    And Tap on 'Next'
    When Login
    Then Verify that user logged in