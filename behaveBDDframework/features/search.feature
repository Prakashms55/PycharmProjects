Feature:  search field functionality
  @completed
  Scenario: verify search functionality with valid product
    Given verify user navigate to the home page
    When user enter the product in the search box
    And user the click the search button
    Then verify user navigate to the product page
  @invalid
  Scenario:  verify search functionality with invalid product
    Given verify user navigate to the home page
    When user enter the invalid product in the search box
    And user the click the search button
    Then verify user get the proper message

 Scenario:  verify search functionality without entering product
    Given verify user navigate to the home page
    When user enter nothing in the search box
    And user the click the search button
    Then proper message should be displayed