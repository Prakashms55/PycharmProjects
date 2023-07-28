Feature: Register the account

  Scenario: verify that user can able to register the account
    Given verify user navigate to the home page
    When user clicks the myaccount element
    And user clicks the register button
    Then verify user navigate to the register page
    And enter the below records in the required field
    |firstname|lastname|email            |telephone|password|reenterpwd|
    | praveen| MSD     |msd123@gmail.com |698765432|password|password|
    And tick the privacy policy and click continue button
    And verify that user launched in account page