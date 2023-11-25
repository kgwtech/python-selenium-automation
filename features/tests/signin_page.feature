Feature: SignIn page UI tests

  Scenario: User can successfully login from Main page
    Given Open target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Input telme0@btcmod.com and ****** on SignIn page
    Then Click Sign In
    Then Verify user is successfully logged in

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Given Store original window
    Then Click on Target terms and conditions link
    When Switch to new window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original

