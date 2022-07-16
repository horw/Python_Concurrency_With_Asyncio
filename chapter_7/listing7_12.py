import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Hello world app')
window.geometry('200x100')


def say_hello():
    print('Hello there!')


hello_btn = ttk.Button(window, text='Say Hello', command=say_hello)
hello_btn.pack()

window.mainloop()