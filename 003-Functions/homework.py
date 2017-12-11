"""
Assignment: Build a command line program to recursively search a directory.

1. Recursively read files in all directories
2. If filename/directory contains word, print it out
3. Provide summary of all files/dirs found with complete path and a score (how many words does it have present)
4. In directories:  <-- this seems lame
	1. count the number of different types of extensions
5. For multiple words, show the directories/files associated with each


### Extra Credit:
* Modify this to look in file contents as well
* To open a file:

```python
with open(filepath) as fh:
    fh.read()
```
"""