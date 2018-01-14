"""
Assignment
===============
* Write a program which repeatedly reads numbers until the user enters "done".
* Once "done" is entered, print out the total, count, and average of the numbers.
* If the user enters anything other than a number, detect their mistake using
try and except and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333
"""
numbers = []
while True:
    data = input('Enter a number: ')
    if data == 'done':
        break
    try:
        number = float(data)
        numbers.append(number)
    except ValueError:
        print('Invalid input')

print('Total =', sum(numbers))
print('Count =', len(numbers))
print('Average =', sum(numbers) / len(numbers))

"""
For extra credit, add the min and max
"""
# long form
maximum = numbers[0]  # start with the first one
minimum = numbers[0]
for number in numbers[1:]:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

# shortcut
print('Min =', min(numbers), minimum)
print('Max =', max(numbers), maximum)
