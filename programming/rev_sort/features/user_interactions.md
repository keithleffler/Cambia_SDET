# BDD scgenarios for user interaction with the program

## Scenario: All good, using the example input, no existing output.

    This is the happy-path scenario, using the example input and output.  This checks
    the basic functionality.  The Cucumber step should check that the output file exists,
    and contains correctly sorted and terminated data.
    
## Scenario: An output file exists and should be over-written

    This scenario checks that an existing test file can be over-written.  The basic purpose of this scenario is to
    ensure that the file write option is correct.
    
## Scenario: The input file does not exist.
    
    This scenario checks that the program fails gracefully when the input file does not exist.  This is unlikely on the 
    developer's desktop, but the following situations could occur:
    
    1. The input file is not included in a distributable file.  Running the unit test from the working directory won't catch 
    this issue.  A framework such as tox, which can rebuild a virtual environment for each run of the unit test will
    identify this issue.  Running unit tests against a Docker image will also find this issue.
    1. The program specifications change slightly to allow the user to input a different input file than input.csv.  
    
## Scenario: The input file exists but user does not have read permissions.

    This scenario checks that the program fails gracefully when the user does not have permission to read the input file.
    Again, this problem won't happen in the example case, but a slight change in requirements to allow the user
    to specify an external file as a command line arguement opens the potential for this problem.
    
## Scenario: The user does not have write permissions for the output location.

    This scenario is the output counterpart to the previous scenario.  A slight change in program requirements
    could allow the user to specify a location without user write permissions.
