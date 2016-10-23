import Tkinter as tk
from Tkinter import *
import ttk

from PIL import Image,ImageTk

LARGE_FONT = ("Verdana", 12)
LARGE_FONT2 = ("Verdana", 20)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bg='black')

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       # label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        #label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.place(x=20, y=80)

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x=20, y=50)

        rvk = Image.open( 'hh.jpg' )
        rvkrender = ImageTk.PhotoImage( rvk )
        img4 = tk.Label( self, image=rvkrender )
        img4.image = rvkrender
        img4.place(x=300, y=20)

        label2 = tk.Label(self, text="Velcome to Infobox your guide\n to the history of Reykjavik\n", font=LARGE_FONT2)
        label2.place(x=480, y=590)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        china = Image.open( 'china.gif' )
        chinar = ImageTk.PhotoImage( china )
        img = tk.Label( self, image=chinar )
        img.image = chinar
        img.place(x=1100, y=600)

        uk = Image.open('uk.gif')
        ukrend = ImageTk.PhotoImage(uk)
        img1 = tk.Label(self, image=ukrend)
        img1.image = ukrend
        img1.place(x=200, y=600)

        germany = Image.open('germany.gif')
        germanrender = ImageTk.PhotoImage(germany)
        img2 = tk.Label(self, image=germanrender)
        img2.image = germanrender
        img2.place(x=500, y=600)

        france = Image.open('France.gif')
        frender = ImageTk.PhotoImage(france)
        img3 = tk.Label(self, image=frender)
        img3.image = frender
        img3.place(x=800, y=600)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Frame = Frame(width=768, height=576, bg="black", colormap="new")

        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()




app = SeaofBTCapp()
app.geometry("2200x700")
app.mainloop()