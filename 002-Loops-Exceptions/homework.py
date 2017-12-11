"""
Assignment: Build a command line program to search for a word in a file.

1. To open a file, here's the code.

```python
with open(filepath) as fh:
    text = fh.read()
```


2. To check if a word is present, you can use a simple `if` statement with `in`


3. To modify the program, count the number of times the word appears in the file


4. (Extra credit) Use any method to find the 5 most frequent words in a file.
(If you need one, use included `dickens.txt`.)

See HINTS at bottom of file for help.
"""


def search(filepath, word):
    count = 0
    # do your work here
    # open file and get text
    # check if the word is present
    print(count)


if __name__ == '__main__':
    # the following allows this to be run from the command line
    import sys
    if len(sys.argv) < 3:
        print('USAGE: python homework.py filepath word_to_find')
    else:
        search(sys.argv[1], sys.argv[2])


"""
HINTS
3a. Idea 1:
```
text = fh.read()
lst = text.split()  # this will split on whitespace
# use a for loop to check for the word
```

3b. Idea 2:
```
text = fh.read()
if word in text:
    idx = text.index(word)  # index at start of word
    idx += len(word)  # index at end of word
    text = text[idx:]
```
But now we need to loop this, and `break` out of the loop when the word is not in the index.

"""
