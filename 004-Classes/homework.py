"""
Assignment: Build a command line program to recursively search a directory.


This is quite complicated, but you can do this if we break it into steps.

Here's a step-by-step look, where each number is a phase. You should have a working program after each phase.

1. Recursively read files in all directories (you need to start with `os.listdir`)
    a. Your function already gives you a directory path and the target word
    b. To get a list of the names of all files and directories in that folder, use os.listdir(path)
    c. Check if the word is in any of those names ("if word in filename")
    d. If it is print the word and filename
2. Recursive element
    a. We need to join the current file or directory (from 1b)
        path_including_file = os.path.join(path, file)
        E.g., os.path.join(r'C:\docs', 'test.txt') => C:\docs\test.txt
    b. We need to check whether the path is a file or directory
        os.path.isfile(path) => returns True if it's a file
        os.path.isdir(path) => returns True if it's a directory/folder
    c. If it's a directory, we call the recurse_directory function with the new path.


### Extra Credit:
* Modify this to look in file contents as well
* To open a file:

```python
with open(filepath) as fh:
    fh.read()
```
"""
import os
import sys


def recurse_directory(path, word):
    pass  # your code here


if __name__ == '__main__':
    path = sys.argv[0]  # this is the first argument
    word = sys.argv[1]  # this is the second argument
    recurse_directory(path, word)

    # tools you can use
    files = os.listdir(path)  # this will list all files/dirs in a directory
    file = files[0]  # the first file in the list
    os.path.isfile(file)  # returns True if item is a file
    os.path.isdir(file)  # returns True if item is a directory (we need to run os.listdir on these)
    os.path.join(path, file)  # joins the paths together

