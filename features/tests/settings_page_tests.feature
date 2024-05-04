# Created by elena.kuletsky at 4/29/2024
Feature: Settings page tests

  Scenario: Verify user can log out of their account
    Given Open The Stunt app
    And Open Settings page
    When Tap 'Logout'
    Then Verify user no longer in their account