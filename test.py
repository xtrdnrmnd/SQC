from tkinter import *

# 1
root = Tk()
# 2
imput_str = StringVar()
Entry(root, textvariable=imput_str).pack()


# 3
def entry_set_call(name, index, mode):
    text = imput_str.get()
    if len(text) > 6:
        imput_str.set(text[:-1])


# 4
imput_str.trace_variable("w", entry_set_call)

# 5
root.mainloop()