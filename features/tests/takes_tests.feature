# Created by elena.kuletsky at 5/7/2024
Feature: Takes tests
  # Enter feature description here

  @smoke
  Scenario: Takes Comment Functionality Test: Ensure Users Can Leave Comments on Takes
    Given Open the app
    When Tap on ‘Takes’ button on the bottom of the screen
    And Select a Take from the list
    And Tap on ‘comment’ icon below the post
    And Enter the comment text in the popup window
    And Tap on ‘Reply’ in the top-right corner
    Then Verify that comment displayed under the Take

  @smoke
  Scenario: Takes Like Functionality Test: Ensure Users Can Like Takes
    Given Open the app
    When Tap on ‘Takes’ button on the bottom of the screen
    And Select a Take from the list
    And Tap on ‘heart’ icon below the post
    Then Verify that number of Likes changed on one more

  @smoke
  Scenario: Takes Forwarding Functionality Test: Ensure Users Can Forward Takes
    Given Open the app
    When Tap on ‘Takes’ button on the bottom of the screen
    And Select a Take from the list
    And Tap on ‘arrow’ icon below the post
    And Select another user from the list
    And Tap on ‘Send’ button
    Then Verify that the Take was successfully sent
