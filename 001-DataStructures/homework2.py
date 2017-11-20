"""
Provide a word as input and then print out how many unique words have been
entered so far.

1. Count the number of unique words provided as input, and provide a report.
2. Change all_words to a dictionary/hashmap, and count the number of times each word appears.
3. Use the str.split() function break up white space given as input.
    * the input "not word" would be treated as two words rather than one
"""

all_words = set()
while True:
    word = input('Give me a word: ')

    print('You have supplies X unique words.')

    # you'll need to exit and run the program again for changes to take effect
    if input('Continue? (y/n): ').lower() != 'y':
        break
