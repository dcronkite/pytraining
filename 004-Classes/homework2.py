"""
Working with recursion.

We're going to explore some common recursion tasks.
While there are often better ways to accomplish these, the practice
    in using functions and understanding recursion is definitely worth
    effort.

Here are a few tasks--don't feel like you need to complete them all.
Just pick the 2 that you find most interesting. As you do more
they will become easier.

The process for solving these is:
1. Establish a "base case". Make this work for the simplest input(s).
    For text, this often looks like 0-1 letters; for numbers, this usually
    means handling then numbers 0 and/or 1.
    Make sure it works with the base case.
2. Now, knowing that you can solve the base case, how would solve the base
    case + 1 (e.g., one additional letter).
    Make sure this works (and that the base case still works)
3. Finally, try to generalize your work in (2).

"""


def factorial(n):
    """
    We did this in class. Calculate the factorial (n! = n * n-1 * n-2 ... * 1)
        of the input number

    Base case:
        0 and 1 both equal 1

    Hint:
        - You can always peak back at 004a-Functions-Complete for hints

    :param n:
    :return: factorial of n
    """
    pass


# Here are some tests
print('Factorial Test:', factorial(0) == 1)
print('Factorial Test:', factorial(1) == 1)
print('Factorial Test:', factorial(2) == 2)
print('Factorial Test:', factorial(10) == 3628800)


def is_palindrome(word):
    """
    A palindrome is a word that has the same letters at the start
        of a word as at the end such that it can be read backwards
        and forwards
        * racecar
        * ana
        * anna
        * evil olive
        * kayak

    Write a function that uses recursion and returns True if it is a
    palindrome, false otherwise. (Yes, you can also do it without recursion.)

    Base case:
        0 or 1 characters (even or odd length) are always true

    Hint:
        - return False as soon as you find a mismatch
        - start from the outside and word your way in
        - remember to lop off two characters at a time

    :param word:
    :return: True if word is a palindrome
    """
    pass


# Here are some tests
print('Palindrome Test:', is_palindrome('') == True)
print('Palindrome Test:', is_palindrome('a') == True)
print('Palindrome Test:', is_palindrome('ab') == False)
print('Palindrome Test:', is_palindrome('bab') == True)
print('Palindrome Test:', is_palindrome('racecar') == True)


def fibonacci(i):
    """
    The fibonacci sequence is a sequence starting with 0, 1, ... in which each subsequent
        value is the sum of the previous two values.

    Fibonacci number:  0  1  1  2  3  5  8  13  21  34
    Sequence's index:  0  1  2  3  4  5  6   7   8   9

    Base case:
        The first number in the sequence is 0
        The second number in the sequence is 1

    Hints:
        - each subsequent number is the sum of the two preceding indices
                so, for some n, we want fibonacci of n-1 + fibonacci of n-2

    Warning:
        - Don't try super large numbers as this method is pretty inefficient.
            I have included a more efficient example in the complete homework

    :param i: integer; requests `i`th number in the fibonacci sequence
    :return: calculated fibonacci number
    """
    pass


# Here are some tests
print('Fibonacci Test:', fibonacci(0) == 0)
print('Fibonacci Test:', fibonacci(1) == 1)
print('Fibonacci Test:', fibonacci(2) == 1)
print('Fibonacci Test:', fibonacci(10) == 55)
print('Fibonacci Test:', fibonacci(11) == 89)
