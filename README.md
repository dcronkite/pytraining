# Python Tutorials

## 000- Introduction/Setup/Install

### Install Python/Anaconda

* https://www.anaconda.com/download/
    * 3.x Version
* Install git too: https://git-for-windows.github.io/

### How to use

* IDEs
    * PyCharm Community
    * PyDev (Eclipse)
    * Visual Studio
* Text editors (Name your file ".py")
    * Visual Studio Code
    * Sublime
    * Atom
    * Notepad++
* Run `python example.py` from command line

# Part 1: Fundamentals

## 001- Data Structures
Introduction to the fundamental datatypes in Python along with the basic data structures. These are the building blocks of Python programs and pre-requisite for using the language.

## 002- Loops/Exceptions

* if/elif/else - no case statements
* For/while loops
* Break/continue/pass
* Exceptions

### Example
The motivating example will either be iterating through a directory structure, or traversing a data file.

## 003- Functions and Iterators
Functions allow code re-use, as well as some other Python *magic* like iterators.

* Function syntax
* Recursion
* Iterators
    * yield statement

## 004- Functions and Classes

### Functions

* Revisit functions with a focus on recursion
* Recursion will help to cement previous learning

### Classes
Introduction to Python objects and object-oriented programming.

* Create a Point class (as on an x-y axis)
* Homework has Card class (deck of cards)
    * Simulate a poker game

### Extra
Datetime - learn how to use the datetime class to create dates/datetimes, as well as to calculate their differences

* Learn how to explore and use the documentation
* Practice using classes

# Part 2: Application

* We will look at applications areas for Python
    * Present various Python libraries
    * Cement fundamentals
    * Do the homeworks for areas you find interesting
* Project: Recursive directory search
    * I will provide a shell application in Project1 folder
    * Through the next lessons, we will add new elements to it

## 005- Strings and Regular Expressions

### Formatting Strings

* How to include any Python variables in a string
* How to handle Windows filepaths

### Regular Expressions

* Brief discussion of how regular expressions work
* Explore `re.match`, `re.compile`, and `re.finditer`

### Extra: Additional String Formatting

* Left/right align
* Float/decimal
* Datetimes

## 006- Idiomatic Python

### List/Dict Comprehensions

* Converting list/dicts idiomatic/python/"colloquial" format

### How to run a Python file
* `sys.argv`
* `argparse`

### Libraries

* Standard library
    * logging
* Other resources

### Extra: Deep dive into iterators

* What exactly is an iterator?
* Build your own iterator

## 007- Parsing Files

### Using an IDE

* Show off an IDE and how to use it

### Beyond the Standard Library
An introduction to packages outside the standard library.

* Finding a library that fits your needs
* Determine quality of library by looking at:
    * Github (how recently updated?)
    * Documentation (tutorials/examples?)
    * Stackoverflow (are people actually using?)
* Using pip/conda
    * Built-in to Anaconda
    * Validate non built-in

### Discovering libraries

* Parse office files
* Build office files

### Extra: Create a summary of Powerpoint files in a directory

## 008- Build a GUI

### Evaluate GUI libraries

### Understanding how the GUI works
* tkinter

### Extra: Build a GUI for our search


## 009- Connecting to Data: SQL

### pyodbc
Understanding basics of connection to a SQL datasource.

### SQLAlchemy
Advanced connections, and using an ORM.

### Writing Code to Ease Use
Setting up SQL Alchemy can unnecessarily complicate basic code, so it can be helpful to write your own 'wrappers' around the code to ease use. Share my own library. Introduce git.


## 010- Building a Website

### Motivating Web Server
Another type of GUI, but with different advantages/disadvantages.

### Introducing Flask
Flask framework.

### Building a Chart Abstraction Interface
Example to show how to build out a website.

## 011- Data Science with Python: Pandas

### Introduction to Pandas Data Structure

* Series
* Dataframe

### Example Dataset
Work with and evaluate a sample dataset.

## 012- Advanced Pandas: Data Cleaning and Visualization
Use a 'dirty' dataset, and show steps to clean and analyze the data. This will provide a detailed look at how to use pandas to pick apart a dataset.

### SQL Equivalents in Pandas

* Grouping
* Aggregation
* Ordering
* Filtering out nulls (`isnull`, `notnull`)

### Data Cleaning

* Using `dropna` and `fillna` to clean nulls

### Basic Plotting

* Plotting with `pandas.DataFrame.plot`

## 013- Data Visualization and Testing

* Getting started in the Python visualization ecosystem
* How to test your Python projects to make sure they're working correctly

### Principles of Visualization

* What makes a good visualization?

### Visualization

* Basics of `matplotlib`
* Other frameworks (e.g., seaborn, plot.ly)

### Extra: Writing Tests in Python

* It is important to know that your code is always doing what you expect, testing solves this problem.
* Introduction to test-driven development.

## 014- Machine Learning and Advanced Python

### Principles of Machine Learning/"AI"

* What is machine learning?
* How does it work?

### Machine Learning using `scikit-learn`

* Outline the basic process of building a `scikit-learn` pipeline!

### Extra: Advanced Python Topics

* functions as parameters
* context managers
* lambdas
* decorators
* "magic methods"
* typing

## 015- NLP and Pygame

* Why is Python so often used with NLP?
* Building games is often a useful means of learning a new language, and pygame is no exception.

### Natural Language Processing Concepts

* What is NLP? How does it work?

### Pygame

* Getting started with building a game in Python
* How building a game can help get a background on Python concepts
