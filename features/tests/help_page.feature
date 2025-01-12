Feature: Help page UI tests

  Scenario: Verify 'Target Help' button UI element is present
    Given Open target help page
    Then Verify 'Target Help' text

  Scenario: Verify search box UI element is present
    Given Open target help page
    Then Enter find order in text field


  Scenario: Verify search button UI element is present
    Given Open target help page
    Then Enter find order in text field
    Then Click search icon button


  Scenario: Verify options box UI elements are present
    Given Open target help page
    Then Verify options box has 6 boxes and 1 grid box


  Scenario: Verify additional resources box UI elements are present
    Given Open target help page
    Then Verify additional resources box has 3 boxes


  Scenario: Verify 'Browse Pages' UI element is present
    Given Open target help page
    Then Verify 'Browse all Help pages' text

  Scenario: User can select Help topic
    Given Open target help page for returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page opened

  Scenario: User can select Help topic (1)
    Given Open target help page for returns
    Then Verify Returns page opened
    When Select Help topic Technical Support
    Then Verify Technical Support page opened


