Feature: Search tests
  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url

  Scenario: User can search for christmas lights
    Given Open target main page
    When Search for christmas lights
    Then Verify search worked for christmas lights
    And Verify christmas+lights in search result url

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url

    Examples:
    |product          |expected_product    |expected_url     |
    |coffee           |coffee              |coffee           |
    |tea              |tea                 |tea              |
    |mug              |mug                 |mug              |
    |christmas lights |christmas lights    |christmas+lights |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for headphones
#    click add to cart button
#    store product name
#    open cart page
#    varify cart has 1 item(s)
#    very cart has correct product
    Then Add item to cart
    Then Verify product is in cart


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for headphones
    Then Verify that every product has a name and an image