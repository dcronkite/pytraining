"""
find_in_directory.py
Recursively iterate through files/directories for specified parameters.
# Steps (for homeworks)
## HW005:
1. Run the file. Go to the containing directory and run:
    `python find_in_directory H:\...`
2. A shell has been created which runs, but it is worth figuring out exactly what
    everything is doing. Include some print statements to see what is happening.
3. Write a regular expression that detects (pick one):
    * a word (hard-code, or supply from command line)
    * PHI (what regular expressions would catch this)
4. Include print statements into the program to record what you found.
    * If the window disappears too quickly, pipe these to a file
        *  `python find_in_directory.py H:\... >> out.log`
    * Instead of printing, write to a file
        # add the paths where something was found to a found_items list
        found_items.append((path, 'Found word'))
        for path, note in found_items:
            with open('out.log', 'w') as out:
                out.write(f'{note} in file {path}'.
## HW006:
1. What additional filetypes can you search for? (csv? sas? html?)
2. You can keep the path updated correctly with `os.path.join(root, file)`
    * try printing this out
## HW007:
1. You have learned how to read in some Office doc types. Try adding them to this file
2. Read SAS7BDAT files too with this library: https://pypi.python.org/pypi/sas7bdat
    * Reach out if you have trouble with the documentation
## HW008:
1. Design (on paper) a GUI with the functionality you want to add
    * You will need a space to specify a directory
    * You will want options to specify:
        * Which files?
        * Which words?
        * Regular expression?
    * You will want to see the output
        * Write to file?
        * Display on form
2. Build one element at a time, and test to make sure it works
"""
import os  # operating system (e.g., file) stuff
import sys  # system-specific parameters
import logging  # logging.basicConfig


def main(search_path, file_extension=None):
    """ <-- this is the documentation for your function
    Search through all directories/files under search_path
        and print results related to a particular search.
    :param search_path: path to search for files
    :param file_extension: file_extension to search for (not yet implemented)
    :return:
    """
    for root, files, dirs in os.walk(search_path):
        # root contains the current directory
        # files- list of all files in current directory
        # dirs- list of all dirs in current directory
        for file in files:
            os.path.join(root, file)  # this function might be useful--what does it do?
            pass  # explore what happens here
        for d in dirs:
            # does the `os.path.join` function work here too?
            pass  # explore what happens here
    # nothing to return-- make sure you print out your results


if __name__ == '__main__':
    args = sys.argv  # command line arguments
    if len(args) > 1:  # args[0] == name of program; args[1:] specified by user
        # args[1]  # first argument supplied -> this should be the path
        # args[2]  # this would be a second argument
        if len(args) > 2:
            main(args[1], args[2])  # this should be the directory into function `main`
        else:
            main(args[1])
    else:
        print('Usage: python find_in_directory.py <path> <file-extension>')
        raise ValueError('ArgumentError: Missing parameter.')