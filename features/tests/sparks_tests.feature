# Created by elena.kuletsky at 5/7/2024
Feature: Spark tests

  @smoke
  Scenario: Sparks Comment Functionality Test: Ensure Users Can Leave Comments on Spark
    Given Open the app
    When Tap on ‘Sparks’ button on the bottom of the screen
    And Select a Spark from the list
    And Tap on ‘comment’ icon from sidebar in the right
    And Enter the comment text in the popup window
    And Tap on ‘Send’ button
    Then Verify that comment displayed under the Spark

  @smoke
  Scenario: Sparks Like Functionality Test: Ensure Users Can Like Sparks
    Given Open the app
    When Tap on ‘Sparks’ button on the bottom of the screen
    And Select a Spark from the list
    And Tap on ‘heart’ icon from sidebar in the right
    Then Verify that number of Likes changed on one more

  @smoke
  Scenario: Sparks Forwarding Functionality Test: Ensure Users Can Forward Sparks
    Given Open the app
    When Tap on ‘Sparks’ button on the bottom of the screen
    And Select a Spark from the list
    And Tap on ‘arrow’ icon from sidebar in the right
    And Select another user from the list
    And Tap on ‘Send’ button
    Then Verify that the Spark was successfully sent