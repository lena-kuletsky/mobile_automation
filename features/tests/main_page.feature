# Created by elena.kuletsky at 5/4/2024
Feature: Main page tests
  Background:
    Given Login

  @smoke
  Scenario: Post Creation Test: Check if users can create Post a Take
    When Tap on Plus button at the bottom of the screen
    And Tap on /Post a Take/ from popup menu
    And Enter text I love sport in the text field
    And Tap on ‘Post’ to publish
    Then Verify that post was published

  @smoke
  Scenario: Follow Test: Test the ability to follow another user
    When Tap on ‘search’ icon
    And Enter text Hammes in the search field
    And Tap on ‘People’ tab under search field
    And Pick account from the list
    And Tap on ‘Follow’ button
    When Tap on Back button
    When Tap on Cancel button
    When Tap on the Avatar in the top-left corner
    When Tap on ‘My Profile’ from the side menu
    When Tap on Following in the My Profile page
    Then Verify that following list reflects the addition


  @smoke
  Scenario: Spark Creation Test: Check if users can create sparks
    When Tap on ‘+’ button at the bottom of the screen
    And Select ‘Create a Spark’ from popup menu
    And Tap on the circular button below to start recording
    And Tap on the  circular button to stop recording
    And Tap on ‘Next’ button
    And Tap on checkmark button below the video
    And Tap on ‘Next’ button
    And Tap on ‘Save’ to answer the question ‘Do you want to save the draft?’
    And Tap on ‘Choose from Gallery’ in the Thumbnail page
    And Select an image from the Gallery
    And Tap ‘Done’ in the top-right corner
    And Populate some text in the text field
    And Tap on ‘done’ on the keyboard
    And Tap on ‘Post’ to publish the Spark
    Then Verify that Spark has been published successfully

  @smoke
  Scenario: Search Functionality Test: Verify Users Can Find Users, Posts, or Sparks
    When Tap on ‘search’ icon in the top-right corner
    And Enter text in the search field
    And Tap on ‘All’, ‘People’, ‘Sparks’, ‘Takes’, ‘Replays’ tabs
    Then Verify that the app displays relevant results