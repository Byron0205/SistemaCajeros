from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

#manejo hilos
from threading import Thread

from apps.login import Login

class BtnCajero(ttk.Frame):
    def __init__(self, parent,number):
        super().__init__(parent)
        self.image = PhotoImage(file='cajero.png')
        self.number = number
        self.parent= parent
        self.enUso= False

        self.create_widgets()

    def create_widgets(self):
        self.container_button1 = ttk.Frame(self)
        self.container_button1.grid(column=0, row=2)

        self.cajero1 = ttk.Button(self.container_button1, image=self.image, padding='8', command=lambda:self.OpenCajero())
        self.cajero1.pack(side='left')

        self.cajero1_label = ttk.Label(self.container_button1, text=f'Cajero {self.number}')
        self.cajero1_label.pack(side='left')

        self.cajero1.config(compound='left')

    def OpenCajero(self):
        window_thread = Thread(target=self.ver_cajero)
        window_thread.start()


    def ver_cajero(self):
        
        login = Login(self.parent)
        #cajero = Cajero(self.parent)

