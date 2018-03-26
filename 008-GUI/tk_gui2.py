import tkinter as tk

import os


class SearchApp:

    def __init__(self, parent):
        self.name = tk.StringVar()
        self.path_var = tk.StringVar()

        self.button = tk.Button(
            parent,
            text='Search',
            command=self.print_hello_world
        )
        self.label = tk.Label(parent, text='Term')
        self.entry = tk.Entry(parent,
                              textvariable=self.name,
                              bg='black',
                              fg='white',
                              font=('Courier', 10, 'bold italic')

                              )
        self.path_label = tk.Label(parent, text='Search Path')
        self.path_entry = tk.Entry(parent,
                                     textvariable=self.path_var)

        # title !
        self.title = tk.Label(
            parent,
            text='My Awesome Search Tool!',
            bg='black',
            fg='white',
            font=('Courier', 20, 'bold italic')
        )

        self.text = tk.Text(parent)
        self.layout()

    def layout(self):
        self.title.grid(row=0, column=0,
                        columnspan=7, sticky='we')
        # row 0: term and term entry
        self.label.grid(row=1, column=0)
        self.entry.grid(row=1, column=1,
                        columnspan=6,
                        sticky='we'
                        )
        # row 1: path, and the path entry
        self.path_label.grid(row=2, column=0)
        self.path_entry.grid(row=2, column=1,
                             columnspan=6,
                             sticky='we'
                             )
        # row 2: blank
        # row 3: buttons
        self.button.grid(row=3, column=6, sticky='we')
        # row 4: text box
        self.text.grid(row=4, columnspan=7)

    def print_hello_world(self):
        path = self.path_var.get()
        term = self.name.get().lower()
        for curr_dir, dirs, files in os.walk(path):
            for filename in files:
                if term in filename.lower():
                    fp = os.path.join(curr_dir, filename)
                    self.text.insert(
                        tk.END,
                        fp + '\n'
                    )


if __name__ == '__main__':
    window = tk.Tk()
    window.title('File Search')
    SearchApp(window)
    window.mainloop()
