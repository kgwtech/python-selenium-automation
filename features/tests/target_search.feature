# Created by prime. at 11/1/23
Feature: Search tests

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search result url

  Scenario: User can see cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty message shown

  Scenario: User can access Sign In
    Given Open target main page
    When Click Sign In button
    Then Verify Sign In form opened

  Scenario: User can add an item to cart
    Given Open target main page
    When Item is added to cart
    Then Verify item is in cart
