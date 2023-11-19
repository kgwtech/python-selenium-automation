Feature: Product detail tests

  Scenario: Verify product colors
    Given Open target product page
    Then Click and verify colors and names of product correspond

#    Struggled completing task 3
  Scenario: Verify products' name and images
    Given Open target main page
    Then Search for headphones
    Then Verify all products display a name
    Then Verify all products display an image