Feature: Login

  Scenario: Successful login
    Given user is in login page
    When user enters "standard_user" username
    And user enters "secret_sauce" password
    And click login
    Then user is redirected to inventory page


  Scenario Outline: Unsuccessful login using different accounts
    Given user is in login page
    When user enters "<username>" username
    And user enters "<password>" password
    And click login
    Then error message "<error_message>" is displayed

    Examples:
      | username        | password     | error_message                                                             |
      | invalid         | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |

  Scenario: Unsuccessful login with no password
    Given user is in login page
    When user enters "standard_user" username
    And click login
    Then error message "Epic sadface: Password is required" is displayed