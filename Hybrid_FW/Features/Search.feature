Feature:  Search functionality

  Scenario: Search for a valid product
    Given I navigate to home page
    When I search for a valid product "HP" in search box
    Then I click on Search button
    Then Product information and details should be displayed

  Scenario: Search for an invalid product
    Given I navigate to home page
    When I search for an invalid product "BMW" in search box
    Then I click on Search button
    Then Proper message should be displayed in search results

  Scenario: Search without entering any product
    Given I navigate to home page
    When I don't enter anything into search box
    Then I click on Search button
    Then Proper message should be displayed in search results