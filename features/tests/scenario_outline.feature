Feature: Search tests

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> search result url
    Examples:
      | product          | expected_product | expected_url     |
      | christmas lights | christmas lights | christmas+lights |
      | coffee           | coffee           | coffee           |
      | tea              | tea              | tea              |

