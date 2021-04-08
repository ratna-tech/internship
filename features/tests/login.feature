# Created by Ratna Sinha at 4/8/2021
Feature: this is to test all Login Page features
  # Enter feature description here

  Scenario: Login page has all UI elements
    Given opens login page
    Then verify email header Username or email address * present
    And verify email textbox present
    And verify password header Password * present
    And verify password textbox present
    And verify header Remember me present
    And verify Remember me checkbox present
    And verify LOG IN button present
    And verify User can see Best Selling, Latest, Top Rated blocks

  Scenario:  User can click on Lost your password link and is taken to password reset form
    Given opens login page
    Then verify Lost your password link present