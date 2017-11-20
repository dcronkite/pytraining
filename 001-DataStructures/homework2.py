"""
1. Count the number of unique words provided as input, and provide a report.
2. Change all_words to a dictionary/hashmap, and count the number of times each word appears.
"""

all_words = set()
while True:
    word = input('Give me a word: ')

    print('You have supplies X unique words.')

    # you'll need to exit and run the program again for changes to take effect
    if input('Continue? (y/n): ').lower() != 'y':
        break
