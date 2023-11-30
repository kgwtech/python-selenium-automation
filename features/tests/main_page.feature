Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target main page
    Then Verify header is present
    Then Verify header has 5 links

  Scenario: User can access Sign In form, from Main Page
    Given Open target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened

  Scenario: User can see signin arrow
    Given Open target main page
    When Hover over signin button
    Then Verify Signin arrow shown


