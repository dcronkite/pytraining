"""
Assignment: Build a command line program to search for a word in a file.

1. To open a file, here's the code

```python
with open(filepath) as fh:
    text = fh.read()
```

2. To check if a word is present, you can use a simple `if` statement with `in`


3. To modify the program, count the number of times the word appears in the file

See HINTS at bottom of file for help.
"""


def search(filepath, word):
    count = 0
    with open(filepath) as fh:
        text = fh.read().lower()  # read case insensitive
    while True:
        if word in text:
            idx = text.index(word)  # index at start of word
            idx += len(word)  # index at end of word
            text = text[idx:]
            count += 1
        else:
            break
    print(count)


def search2(filepath, word):
    count = 0
    with open(filepath) as fh:
        text = fh.read().lower()  # read case insensitive
    for w in text.split():
        if word in w:
            count += 1
    print(count)


def search3(filepath, word):
    import re  # regular expression library
    count = 0
    with open(filepath) as fh:
        text = fh.read().lower()
    for m in re.finditer(word, text, re.IGNORECASE):
        count += 1
    print(count)


if __name__ == '__main__':
    # the following allows this to be run from the command line
    import sys
    if len(sys.argv) < 3:
        print('USAGE: python homework.py filepath word_to_find')
    else:
        search(sys.argv[1], sys.argv[2])
        search2(sys.argv[1], sys.argv[2])
        search3(sys.argv[1], sys.argv[2])
