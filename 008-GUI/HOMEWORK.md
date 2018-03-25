
## Homework ##

### Reminders/Hints ###
* My solutions are in the `tk_gui_complete.py` file
* Run your code by doing:
    * `python C:\wksp\project\tk_gui.py`
* Test your code after making even small changes
    * Use git to take snapshots of working code
        * `git add file_i_modified.py` 
        * `git commit -m "The changes I just made"`
* Add comments to make your code/intentions easier to read 

### Homework Ideas ###
* Count how many files matched and output that at the end
* Add a clear button to clear window contents
    * `self.text.delete(1.0, tk.END)`  # for Text object, index starts at "1" and goes to the END
    * `self.entry.delete(0.0, tk.END)`  # for Entry object, index starts at "0" and goes to the END
* Add a button to write window output to a file
    * Get the content of the Text object with:
        * `self.text.get(1.0, tk.END)`  # from index "1" to the END
* `__init__` method is getting crowded, move these into a "layout" function
    * Remember to call the `layout` function from inside `__init__`
* Add color to your application by passing these values in when creating the Entry/Label objects:
    * bg="black"
    * text="white"
    * font=('Courier', 14, 'bold')
* What happens when you input bad data?
    * Check for bad data, then alert the user.
    * Here are some helpful methods:
        * `os.path.isfile`
        * `os.path.isdir`
* Having trouble reading your code/editing?
    * Add additional comments to improve readability/improvements
    * After a method function, put a description of what it does in triple quotes:
        `"""looks for files with a particular extension"""`
* Use checkboxes to search for multiple file extensions at once
    * `this.sas_checked = tk.IntVar()`
    * `this.checkbutton = tk.Checkbutton(parent, text='sas', variable=sas_checked)`
    * `if this.sas_checked.get():  # button is checked`