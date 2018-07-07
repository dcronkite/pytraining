# Python Testing

We will be using pytest. This is probably both the easiest testing framework
to get started with, while having a variety of useful advanced features.
Pytest comes with Anaconda if you used that distribution to install
Python.

Testing is a _very_ important component of writing code. Without testing,
how do you know that your function, macro, regular expression, etc.,
do what you want them to do?

Testing supplies your function/macro/regex/etc. with a series of inputs
and compares the outputs to what you expect to get back. If you make
changes, you can re-run all your tests to make sure that everything
still behaves as before.

## Intro to Testing

To run pytest:

1. Create an file called `test_[your name here].py`
2. Create a function in the file:
    ```
    def test_something():
        assert (1, 2, 3) == (1, 2, 3) 
    ```
3. Open up command line in the directory containing this file, and run `pytest`.

## Test-driven Development

Test-driven development (TDD) is method for building an functionality by
testing every tiny change. A workflow might look like this:

1. Write a test for how you want to use your function
2. Run your tests -- they will fail
3. Make your tests NOT fail
4. Repeat
