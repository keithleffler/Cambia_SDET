# Cambia_SDET

Respository for Cambia Take-Home exercise.


## Problem Statement


_The solution must be runnable with a Docker command (i.e., include a Dockerfile)._

Imagine a CSV file called input.csv, which contains a single line of comma-separated strings. This
single line is terminated with a new line character. Using Python, write a program that reads
input.csv, sorts its strings into descending alphabetical order, and writes the sorted strings in
comma-separated format to a new file called output.csv.
Here are sample contents of these two files (but your program should handle other content as well):

• input file: Copenhagen,Stockholm,Oslo

• output file: Stockholm,Oslo,Copenhagen


## Solution

Code for the solution can be found in  /programming/rev_sort

    The solution can be run with the following:
    
    > cd ./programming/rev_sort
    
    > docker build -t rev_sort .
    
    > docker run rev_sort:latest


## Gherkin questions
* [Gherkin questions](./gherkin.md#Gherkin)     
 

## Tools questions
* [Tools Questions](./tools_questions.md#Tools)             

## Testing questions
* [Testing Methods Questions](./methods_questions.md#Methods)   

