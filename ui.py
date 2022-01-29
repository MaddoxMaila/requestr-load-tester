from itertools import count
from tkinter import *
from requestr import Requestr

req = Requestr()

class UI :

    REQ_MSG = None
    REQ_URL = None

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
        self.buttons()

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

    def buttons(self) -> None:

        self.make_req_btn = Button(
            self.inputs_frame,
            text="Start Load Test",
            command=lambda: self.req_btn_handle(self.url_text_entry.get())
        ).grid(
            row=6,
            column=0,
            columnspan=2
        )
    
    def req_btn_handle(self, url: str):
        
        if url == "":
            print("URL Empty")
        else:
            req.set_req_url(url)
            req.start()
            # self.REQ_MSG, self.REQ_URL = req.make_request(url=url)
            # print(self.REQ_MSG)
            # print(self.REQ_URL)

