# Created by prime. at 11/9/23
Feature: Target circle page UI tests

  Scenario: User can access circle page
    Given Open target main page
    Then Navigate to Circle page
    Then Verify circle page is displayed

  Scenario: Benefits are visible to user
    Given Open target main page
    Then Navigate to Circle page
    Then Verify 5 benefit boxes are displayed
