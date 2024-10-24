Feature: Register Account Functionality

  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name|last_name|telephone |password|
      |Ram       |Test     |1234567890|12345   |
    And I select Privacy policy option
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter below details into all fields
      |first_name|last_name|telephone |password|
      |Ram       |Test     |1234567890|12345   |
    And I select Privacy policy option
    And I click on continue button
    Then Account should get created

  @Test
  Scenario: Register with a duplicate mail address
    Given I navigate to Register Page
    When I enter below details into all fields except mail field
      |first_name|last_name|telephone |password|
      |Ram       |Test     |1234567890|12345   |
    And I enter existing accounts email as "sampletestram@gmail.com" into email field
    And I click on continue button
    Then Proper warning message should be displayed as "Warning: E-Mail Address is already registered!"


  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning message for all fields should be displayed