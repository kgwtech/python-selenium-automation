Feature: Circle page UI tests

  Scenario: User can access circle page from main page
    Given Open target main page
    Then Navigate to Circle page
    Then Verify circle page is displayed

  Scenario: Benefits are visible to user from main page
    Given Open target main page
    Then Navigate to Circle page
    Then Verify 4 tabs are displayed


  Scenario: User can open circle page
    Given Open target Circle Page
    Then Verify circle page is displayed

  Scenario: User can click through Page tabs
    Given Open target circle page
    Then Verify user can click through tabs

  Scenario: User is able to navigate to Google Play Target
    Given Open target Circle Page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    Then Return to original window


