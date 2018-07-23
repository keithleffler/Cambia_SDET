# Created by leffler at 7/21/18
Feature: User interaction with the program from the command line

  In oder to sort comma separated values in an input file and write the results to an output file,

  As a user, I want to know when the program has succeeded.  If there is a failure, I want a helpful
  message that will help me run the program successfully.

  The first scenario is the only one that's strictly required by the assignment.  However, I've added scenarios that
  could be encountered by packaging the application as a Docker file or binary distribution, or when moving testing
  to an different environment that the developer's desktop.

  Scenario: All good, using the example input, no existing output file

    Given the input file exists
    And user can read the input file
    And the user can write to the output path
    And the output file does not exist

    When the user runs the program with example input

    Then  the output file should contain the example output

  Scenario: An output file exists and should be overwritten when the program runs.

    Given an output file already exists
    And the user can write to the output file

    When the user runs the program with example input

    Then the output file should contain the example output
    And  the output file should be newer than the old one

  Scenario: Input file does not exist

    Given the input file is missing
    When the user runs the program with example input
    Then the program should tell the user the file does not exist

  Scenario: Input file exists but user does not have read permission.

    Given the input file exists
    But the user does not have read permissions
    When the user runs the program with example input
    Then the program should tell the user that "she" does not have adequate permission to "read the input file"

  Scenario: User does not have write permissions for the output location.

     Given the user does not have write permission to the output path
     When the user runs the program with example input
     Then the program should tell the user that "he" does not have adequate permission to "write the output file"

