# Created by elena.kuletsky at 4/29/2024
Feature: Create Post tests

  Scenario: Create a Post
    Given Open The Stunt app
    When Tap plus button
    And Select 'Post a Take' option
    And Populate text
    And Tap 'image' icon
    And Select 4 pictures from Gallery
    And Tap 'Add' button
    And Tap 'Post' button
    Then Verify Post is published