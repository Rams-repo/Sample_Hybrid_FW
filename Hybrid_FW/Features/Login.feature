Feature: Login Functionality

  @Test
  Scenario Outline: Login with valid credentials
    Given I navigate to Login page
    When I enter valid email id as "<email>" and password as "<password>"
    Then I click on login button
    Then I should login to home page as "My Account"
    Examples:
      | email                    | password |
      | sampletestram@gmail.com  | 12345    |
      | sampletestram1@gmail.com | 123456   |

  Scenario: Login with invalid email and valid password
    Given I navigate to Login page
    When I enter invalid email id and valid password as "12345"
    Then I click on login button
    Then I should get a proper warning message as "Warning: No match for E-Mail Address and/or Password."


  Scenario: Login with valid email and invalid password
    Given I navigate to Login page
    When I enter valid email id as "sampletestram@gmail.com" and invalid password as "Test"
    Then I click on login button
    Then I should get a proper warning message as "Warning: No match for E-Mail Address and/or Password."


  Scenario: Login with invalid credentials
    Given I navigate to Login page
    When I enter invalid email id and invalid password as "Test"
    Then I click on login button
    Then I should get a proper warning message as "Warning: No match for E-Mail Address and/or Password."


  Scenario: Login without entering any credentials
    Given I navigate to Login page
    When I dont enter email id and password
    Then I click on login button
    Then I should get a proper warning message as "Warning: No match for E-Mail Address and/or Password."