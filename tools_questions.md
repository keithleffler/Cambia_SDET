# Tools


## Question 1
_In your opinion, what’s helpful about version control systems? What’s annoying about them?_

__Helpful__
* They allow multiple developers to work on the same project simultaneously, without over-writing other's work.
* They provide a (hopefully) safe backup for files, including history of every change for every file.
* Some systems allow individual developers to keep multiple versions of the same code base.

__Annoying__
* Binary files are not always handled well.  This sometimes creates a need for a separate location(s)
to store binary files.
* Developers may be able to alter or revert a lot of other people's work, sometimes purposely, sometimes by accident.
* It is possible to keep changes on branches for too long, and the changes become difficult or impossible to re-integrate.
The version control system can create false confidence that large code changes can _eventually_ be integrated.


## Question 2

_What are some pros and cons of using Docker to develop, test, and deploy software?_

__Pros__
* Applications are portable to any environment supporting Docker.
* There is an incentive to break monolithic applications into a collection of Docker applications, each supporting 
a single feature.
* It facilitates service-oriented architectures.

__Cons__
* Developers may require a change in mindset, and additional training. (This could be seen as a Pro)
* Developing for Docker adds another layer of complexity over an application installed into the host operating system.


## Question 3
_How do you choose which language to use for a given task?_

1. Choose a language, or at least a language type, that supports the problem space.  The Java or .NET frameworks be good choices 
for writing enterprise applications.  Though possible, low level C would involve a lot of extra work.  
2. Once a language class is determined, choose a technology stack that fits the customer.  Microsoft technologies may not be 
the best choice for an organization that relies solely on Unix and Java.
3. Choose a language within the identified class and technology stack that the developers know well, or can learn with enough time to complete the project.

 _How did you choose the language for the programming exercise above?_
 
 __The instructions specified that the exercise must be completed using Python.__
 
