# Methods


[Return to README](./README.md#Cambia_SDET)

## 1. _What’s the right role for QA in the software development process?_

QA's basic role is to provide a measurement of software's readiness to ship.  This basic function can be performed differently 
in different organizations, but the core role is to help all stakeholders understand readiness to ship. 
    
## 2. _As a QA person, you have 2 weeks to prepare before your team starts writing software. What do you do?_

I would ask a lot of questions:
*  What is the software supposed to do?  
    QA needs to understand what the system is supposed to do, to ensure that the developers create the Right Thing.
* How do the designers intend to implement the software.  
    QA need to understand how all the pieces will fit together, or least the current plan.  QA needs to understand how
    to identify correct and undesired system behavior, to ensure that the Thing is Right.
* How will QA measure the system's readiness to ship?
    This includes developing tests and automation, arranging for manual testing, and agreeing with project stakeholder on
    metrics.  The team needs to agree on how to communicate that the Right Thing is being built, and the Thing will be 
    Right when it's Done.

While working on getting answers to these questions, I would work with the project team to build testability into
their process.  This is the best time to agree on coding standards, requirements acceptance criteria, and unit testing
practices for the project
   
## 3. _When is it appropriate to use automated testing? When is it appropriate to use manual testing?_

In short, it is appropriate to use automated testing whenever the return on investment of automation development 
is positive, but this is easier said than done.
        
__Manual testing__

Manual testing is well suited for many types of testing, including:

* Ad-hoc testing:  These are testing tasks that occur once or infrequently.  The effort to automate this type of testing
far exceeds the effort to simply execute the test. Ad-hoc tests may eventually become candidates for automation if
they are executed more regularly as software development continues.

* Exploratory testing:  These tests usually do not have enough structure to define test steps.  The tester is usually 
trying to find out what happens after an action or sequence of actions.  The results of exploratory testing can lead
to more formalized tests, especially if unexpected results occur.

* Usability testing and user experience:  Automated tests can be developed to check if user interactions function _as
designed_.  This does not indicate if software in pleasant to use.  It is advisable to invest in user experience design
early in a project, and test UI wireframes as soon as possible in the project.  The user experience should be tested 
on release candidate software before release.

__Automated testing__

Automated testing is appropriate when desired and incorrect behavior can be fully described, and the return on investment
is positive.  These situations include:

* API testing.  This is testing an interface, where the input and expected output can be specified and compared autoamtically.
* UI testing where the sequence of actions and responses is known.
* Regression testing, where a system is known to be working, and testing is needed to ensure it continues to work as before.
    
## 4. _Your dev team has just modified an existing product by adding new features and refactoring the
code for old features. The devs claim to have written unit tests; you’re in charge of integration
testing. Dedicated teams are handling performance and security testing, so you don’t have to. As
is always the case in the real world, you don’t have time to test everything. What factors do you
think about as you decide where to focus your testing efforts? How do you decide what not to
test?_

My basic strategy would be to identify the greatest risks, and concentrate testing in those areas.  High-yield, 
low-effort testing can also be identified and put into the test plan.

__Things to ask:__

* Where are the greatest risks, and how can these be tested?

* How good is the dev's claim - Run or ask for a coverage report?  Gaps in unit testing can be sent back to dev while
testing proceeds in parallel.

* Is there previous test automation that can be used to execute regression testing on existing modules?  Hopefully there
is something existing that can be used or adopted.


__Things to test__

* New code modules. These should be tested as heavily as time allows, with an emphasis on the highest-risk areas

* Deployment of new and existing modules together.  Containers help isolate system components, and ease the test load here.

* Data and communication flows between new and existing components.
   
__Things that end up on the bottom of the list__ 

Internal (white/grey box) test of previously stable code,.  The assumption is that un-modified modules
should continue to work, provided they can handle communication with newer modules and deployment in the new 
production environment.

[Return to README](./README.md#Cambia_SDET)
