from queue import Queue
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from typing import Optional
from chapter_7.listing7_13 import StressTest


class LoadTester(Tk):

    def __init__(self,loop,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self._queue = Queue()
        self._refresh_ms = 25

        self._loop = loop
        self._load_test: Optional[StressTest] = None
        self.title('Url Requester')

        self._url_label = Label(self, text="URL:")
        self._url_label.grid(column=0,row=0)

        self._url_field = Entry(self, width=10)
        self._url_field.grid(column=1, row=0)

        self.