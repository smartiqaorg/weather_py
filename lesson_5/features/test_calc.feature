# Feature file
Feature: Calculator Test

  Background:
    Given a calculator

  @sum
  Scenario: Test addition of 2 numbers
    When first number is 7
      And second number is 10
    Then the sum of the numbers is 17

  @sub
  Scenario Outline: Test subtraction of 2 numbers
    When first number is <a>
      And second number is <b>
    Then the subtraction of the numbers is <sub>

    Examples:
    | a  | b | sub |
    | 20 | 0 | 20  |
    | 20 | 1 | 19  |
    | 20 | 5 | 15  |