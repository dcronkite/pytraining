import tkinter as tk

import os


class SearchApp:

    def __init__(self, parent):
        self.intvar = tk.IntVar()
        self.path = tk.StringVar()
        self.path_label = tk.StringVar()
        self.path_label.set('Path')
        self.label = tk.Label(parent, textvariable=self.path_label)
        self.label.pack()
        self.entry = tk.Entry(parent, textvariable=self.path)
        self.entry.pack()
        self.ext = tk.StringVar()
        self.ext_label = tk.StringVar()
        self.ext_label.set('Extension to Find')
        self.label2 = tk.Label(parent, textvariable=self.ext_label)
        self.label2.pack()
        self.entry2 = tk.Entry(parent, textvariable=self.ext)
        self.entry2.pack()
        self.run_button_label = tk.StringVar()
        self.run_button_label.set('Run')
        self.button = tk.Button(parent, textvariable=self.run_button_label,
                                command=self.find_pptx_files)
        self.button.pack()
        self.tk_text = tk.Text(parent)
        self.tk_text.pack()

    def add_text(self):
        self.tk_text.insert(tk.END, self.path.get() + '\n')

    def find_pptx_files(self):
        for curr_dir, dirs, files in os.walk(self.path.get()):
            for file in files:
                if file.endswith(self.ext.get()):
                    fp = os.path.join(curr_dir, file)
                    self.tk_text.insert(tk.END, fp + '\n')


def print_hi():
    print('Hi!!')

if __name__ == '__main__':
    window = tk.Tk()
    SearchApp(window)

    # name = tk.StringVar()
    # up_button = tk.IntVar()
    # label = tk.Label(window, textvariable=name)
    # label.pack()
    # entry = tk.Entry(window, textvariable=name)
    # entry.pack()
    # button = tk.Button(window, textvariable=name, command=print_hi)
    # button.pack()
    # text = tk.Text(window)
    # text.insert(tk.END, 'hello')
    # text.pack()

    window.mainloop()
