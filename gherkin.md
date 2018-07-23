## Gherkin



## Question 1
_Write Gherkin tests for the program you wrote above. Use any Gherkin features or practices you
want. Don’t write step definitions (i.e., the tests don’t have to be executable)._

    The feature files are located in /programming/rev_sort/features

## Question 2
_Explain in detail why these tests might be helpful in the future._

A program that sorts a single string from a fixed input file is not particularly interesting on it's own, but may be expanded 
in the future. I had two scenarios in mind when writing this code.  

The first is flexibility in file location.  Packaging the program into a Docker image or binary file requires 
adding input.csv into a setup file.  Checking for presence of the file ensures that program is portable.  The unit tests
should be executed in an isolated environment such as Docker of a Python virtual environment.  Execution of unit tests
in a working directory won't catch this type of problem.  A natural addition to the requirements is allowing the user the user to specify the input and
output files.  File existence, and file permissions issues can occur here, so additional checks for existence and readability 
follow.   Files may be located locally, on a network, or in a cloud location.  Location flexibility is to be expected
as an application grows in scope.

Allowing the user to specify the input file allows the user to control file content, and the  states that the program should be able to handle different content.  
I realized at this point that Python's sorting method may not match the users expectation, and the problem does not define 
user expectations.  Several of the scenarios in sorting.feature  identify situations where the default sorting order may not be desirable.  
I've added steps asking the programmer to ask for more clarification.  Projects may use other software to track requirements, but
including points of clarification builds it into the requirements, and keeps the issue in front of all stakeholders.
Once the behavior is clarified, new tests can be written and code modified to implement the desired behavior.  The clarification
steps of the feature would be removed. 

I also built in tests for handling white space.  Supported input formats may change, but the need to input validation will remain.  The identified issues
with a simple output may raise the issue of input validation with stakeholders.

To aid future modification, existing feature files document the current functionality of the system. Existing, passing unit tests that 
cover the code serve as a foundation for future modifications.  The existing feature definitions, (unwritten) feature tests,
and base unit tests serve as a foundation for future additons to the code.



