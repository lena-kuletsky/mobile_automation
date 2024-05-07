# Created by elena.kuletsky at 5/4/2024
Feature: Main page tests

  @smoke
  Scenario: Post Creation Test: Check if users can create Post a Take successfully
    Given Open the app
    When Tap on ‘+’ button at the bottom of the screen
    And Select ‘Post a Take’ from popup menu
    And Enter text in the text field
#    And Tap on ‘image’ icon below
#    And Select one picture from the Gallery
#    And Tap on ‘Add’ in the top-right corner
#    And Tap on ‘Post’ in the top-right corner
    Then Verify that post was published successfully

  @smoke
  Scenario: Follow Test: Test the ability to follow another user and verify that the action is reflected in the follower's list
    Given Open the app
    When Tap on ‘search’ icon in the top-right corner
    And Enter text in the search field
    And Tap on ‘People’ tab under search field
    And Select any account from the list
    And On the account's page, tap ‘Follow’ button
    When Go back to user’s profile ???
    Then Verify that follower's list reflects the addition


  @smoke
  Scenario: Spark Creation Test: Check if users can create sparks successfully
    Given Open the app
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
    Given Open the app
    When Tap on ‘search’ icon in the top-right corner
    And Enter text in the search field
    And Tap on ‘All’, ‘People’, ‘Sparks’, ‘Takes’, ‘Replays’ tabs
    Then Verify that the app displays relevant results