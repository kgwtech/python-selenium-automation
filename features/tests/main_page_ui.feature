# Created by prime. at 11/9/23
Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target main page
    Then Verify header is present
    Then Verify header has 5 links
