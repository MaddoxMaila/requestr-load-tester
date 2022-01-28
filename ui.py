from cgitb import text
from tkinter import *


class UI :

    def __init__(self) -> None:
        self.main = Tk()
        self.display_window()


    def display_window(self) -> None:
        self.main.maxsize(width=400, height=400)
        self.main.minsize(width=400, height=400)

        self.main.title = "IntelliBRAINs Load Tester"

        self.frames()
        self.labels()
        self.entry_vars()
        self.intries()

    def show(self) -> None:
        self.main.mainloop()

    def frames(self) -> None:

        self.main_frame = Frame(self.main)
        self.main_frame.pack()

        self.inputs_frame = Frame(self.main_frame)
        self.inputs_frame.pack(side=TOP)

    def labels(self) -> None:
        self.url_label = Label(
            self.inputs_frame,
            text="Url to Server"
        ).grid(
            row=4,
            column=0
        )

    def entry_vars(self) -> None:

        self.url_text_entry = StringVar()
        self.num_reqs_entry = StringVar()

    def intries(self) -> None:

        self.url_entry = Entry(
            self.inputs_frame, 
            textvariable=self.url_text_entry
        ).grid(
            row=4,
            column=1,
            ipadx=70,
            ipady=10
        )

