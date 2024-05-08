# Created by elena.kuletsky at 5/7/2024
Feature: My Profile tests

  @smoke
  Scenario: Post Deletion Test: Verify that users can delete their own posts
    Given Open the app
    When Tap on the Avatar in the top-left corner
    And Tap on ‘My Profile’ from the side menu
    And Tap on ‘Takes’ tab
    And Select post
    And Tap on the three-dot button in top-right corner
    And From the popup window that appears, tap ‘Delete this post’ option
    Then Verify that the message 'Your post has been deleted' is displayed


  @smoke
  Scenario: Unfollow Test: Verify that users can unfollow someone and ensure that the action is reflected in the follower's list
    Given Open the app
    When Tap on the Avatar in the top-left corner
    And Tap on ‘My Profile’ from the side menu
    And Tap on ‘Following’ under profile description
    And Select an account from the list
    And Tap on ‘Following’ to unfollow
    Then Verify that the app updated the follower's list in the Profile page

  @smoke
  Scenario: Spark Deletion Test: Verify that users can delete their own sparks
    Given Open the app
    When Tap on the Avatar in the top-left corner
    And Tap on ‘My Profile’ from the side menu
    And Tap on ‘Sparks’ tab
    And Select a Spark
    And Tap on the three-dot button in the right sidebar
    And From the popup window that appears, tap on ‘Delete this spark’ option
    Then Verify that the message 'Your post has been deleted' is displayed

  @smoke
  Scenario: Profile Update Test: Verify users can update their profile information successfully
    Given Open the app
    When Tap on the Avatar in the top-left corner
    And Tap on ‘My Profile’ from the side menu
    And Tap on ‘Avatar’ in the top-right corner
    And Select “Select From Gallery’ option and choose a picture from the Gallery
    And Tap on ‘Edit’
    And Tap on ‘Edit Banner
    And Select “Select From Gallery’ option and choose a picture from the Gallery
    And Tap on the Title field and edit the text
    And Tap ‘done’
    And Tap on the Description field and edit the text
    And Tap ‘done’
    And Tap on ‘Update’ button in the low-right corner
    Then Verify that the user’s profile successfully updated

