"""
Run this file from the command line by going to the directory
and typing:
python homework1.py


Assignment
=============
Take two numbers and combine them according to the given operation.
I've started it...

Hint: Input returns a `str`, and the numbers need to be `int` or `float` to combine them.
"""
while True:  # this lets you do several iterations
    num1 = input('Give me a number: ')
    num2 = input('Give me another number: ')
    operator = input('Give me an operator: ')

    if operator == '+':
        print(num1 + num2)  # this is wrong to start
    elif operator == '-':
        print(num1 - num2)
    else:
        print('I did not recognize the operator.')

    # you'll need to exit and run the program again for changes to take effect
    if input('Continue? (y/n): ').lower() != 'y':
        break
