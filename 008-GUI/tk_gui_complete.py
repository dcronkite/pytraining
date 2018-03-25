"""This is a common place to describe what a file does/is used for.

Python application that recursively searches for a set of
    extensions and reports those as output.
"""
import tkinter as tk

import os

import datetime
from tkinter import filedialog


class SearchApp:

    def __init__(self, parent):
        self.parent = parent
        self.layout()

    def layout(self):

        self.create_widgets()
        self.label.grid(row=1, column=0)
        self.ext_label.grid(row=2, column=0)
        self.entry.grid(row=1, column=1, columnspan=2, sticky='ew')
        self.path_button.grid(row=1, column=3, sticky='ew')
        self.ext_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
        self.run_button.grid(row=4, column=1)
        self.clear_button.grid(row=4, column=2)
        self.write_file_button.grid(row=4, column=3)
        self.tk_text.grid(row=5, column=0,
                          rowspan=6, columnspan=4)
        self.sas_check.grid(row=3, column=0)
        self.csv_check.grid(row=3, column=1)
        self.xlsx_check.grid(row=3, column=2)

    def create_widgets(self):
        """
        Create widgets used in the UI
        1. widget to capture path variable
        2. widget to get the extension

        :return:
        """
        # path variable
        self.path = tk.StringVar()
        self.label = tk.Label(self.parent, text='Path')
        self.entry = tk.Entry(self.parent, textvariable=self.path)
        self.path_button = tk.Button(self.parent, text='Choose Path',
                                     command=self.get_filepath_from_dialog
                                     )

        # extension variable
        # added checkboxes as well
        self.ext = tk.StringVar()
        self.sas_var = tk.IntVar()
        self.sas_check = tk.Checkbutton(self.parent, text='sas7bdat', variable=self.sas_var)
        self.csv_var = tk.IntVar()
        self.csv_check = tk.Checkbutton(self.parent, text='csv', variable=self.csv_var)
        self.xlsx_var = tk.IntVar()
        self.xlsx_check = tk.Checkbutton(self.parent, text='xls(x)', variable=self.xlsx_var)
        self.ext_label = tk.Label(self.parent, text='Extension(s) to Find')
        self.ext_entry = tk.Entry(self.parent, textvariable=self.ext)

        # run button
        self.run_button_label = tk.StringVar()
        self.run_button_label.set('Run')
        self.run_button = tk.Button(self.parent, textvariable=self.run_button_label,
                                    bg='Green',
                                    width=20,
                                    command=self.find_files_by_ext)

        # clear button
        self.clear_button_label = tk.StringVar()
        self.clear_button_label.set('Clear')
        self.clear_button = tk.Button(self.parent,
                                      textvariable=self.clear_button_label,
                                      bg='Red',
                                      width=20,
                                      command=self.clear_log_console
                                      )

        # write to file button
        self.write_file_button_label = tk.StringVar()
        self.write_file_button_label.set('Log to File')
        self.write_file_button = tk.Button(self.parent,
                                           textvariable=self.write_file_button_label,
                                           bg='Yellow',
                                           width=20,
                                           command=self.write_log_to_file
                                           )

        # logging console
        self.tk_text = tk.Text(
            self.parent,
            bg='black', fg='white',
            font=('Courier', 16, 'bold')
        )

    def _log(self, text, header=''):
        """
        Simple method to log output and add endlines, etc.
        :param text: text to output; newline automatically added
        :param header: text to precede the output (timestamp, "ERROR")
        :return:
        """
        text = f'{header}:\t{text}\n' if header else f'{text}\n'
        self.tk_text.insert(tk.END, text)

    def get_filepath_from_dialog(self):
        """

        :return:
        """
        self.path.set(filedialog.askdirectory())

    def find_files_by_ext(self):
        """
        Identify files by their extension and output them to the log window
        :return: 
        """
        # make sure path is valid
        path = self.path.get()
        if not path.strip():  # empty string
            self._log('No path specified, using current path', 'WARNING')
            path = os.curdir
        if not os.path.isdir(path):  # path isn't a directory
            self._log(f'Path does not exist: "{path}"', 'ERROR')
            return  # don't do any more processing

        # get the extension(s)
        exts = set()  # in case of duplicates
        if self.ext.get():  # user-typed extension
            exts.add(self.ext.get())
        if self.xlsx_var.get():
            exts.add('xlsx')
            exts.add('xls')
        if self.sas_var.get():
            exts.add('sas7bdat')
        if self.csv_var.get():
            exts.add('csv')

        if not exts:  # no extensions to look for
            self._log(f'No extensions to search for.', 'ERROR')
            return

        # do the search itself
        count = 0  # track how many found
        for curr_dir, dirs, files in os.walk(path):
            for file in files:  # look through the files
                for ext in exts:  # look for each extension
                    if file.endswith(ext):
                        count += 1
                        fp = os.path.join(curr_dir, file)
                        self._log(fp)
                        break  # don't keep looking through extensions
                        # this will only exit 1 for-loop, so we're back in
                        # `for file in files`
        self._log(f'Found {count} documents.', 'INFO')

    def write_log_to_file(self):
        """
        Write log console to file, include a header with timestamp
        :return:
        """
        text = self.tk_text.get(1.0, tk.END)
        with open('log.txt', 'a') as out:
            out.write('Console log from ')
            out.write(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
            out.write(':\n')
            out.write(text)
            out.write('\n')

    def clear_log_console(self):
        """
        Delete text in logging console
        :return:
        """
        self.tk_text.delete(1.0, tk.END)


if __name__ == '__main__':
    # initialize application
    window = tk.Tk()
    window.title('Search Application')
    SearchApp(window)
    window.mainloop()
