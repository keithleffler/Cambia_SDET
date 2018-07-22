# Created by leffler at 7/21/18
Feature: Sort a CSV string in descending order.

  In order to sort a comma-separated string in reverse order
  As a program user, I want to know the program sorts valid input, am not unpleasantly surpised by strange orderings.

  As a programmer, I see there are some ambiguities in the desired output, but I need to write code before I can
  get answers to all my questions.

  Scenario: All good, using the example values.

    Given the input file exists
    And   the user has permission to read the input file
    And   the user can write to the output file

    When the user runs the program with input  "Copenhagen,Stockholm,Oslo"

    Then the output should be "Stockholm,Oslo,Copenhagen"


  Scenario: Leading Spaces in the input.
    Given the input file exists
    And   the user has permission to read the input file
    And   the user can write to the output file

    When the user runs the program with input "Copenhagen, Stockholm,  Oslo"

    Then the output should be "Stockholm,Oslo,Copenhagen"

    But the programmer should ask for clarification of "How should leading spaces be handled?"

  Scenario: Internal Spaces in the Input
    Given the input file exists
    And   the user has permission to read the input file
    And   the user can write to the output file

    When the user runs the program with input "Copenhagen Denmark,Stockholm Sweden,Oslo Norway"

    Then the output should be "Stockholm Sweden,Oslo Norway,Copenhagen Denmark."
    
  Scenario: Some values start with a number.
    Given the input file exists
    And the user has permission to read the input file
    And the user can write to the output file
    
    When the user runs the program with input "Copenhagen,2 Stockholm,Oslo"
    
    Then the programmer should ask for clarification of "How should leading numbers be handled by the sort?"

  Scenario: Some strings start with lower case.
      Given the input file exists
      And   the user has permission to read the input file
      And   the user can write to the output location

      When the user runs the program with input "Copenhagen,stockholm,oslo"

      Then the programmer should ask for clarification of "How should a leading lower case character be handled?"