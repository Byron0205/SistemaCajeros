from tkinter import ttk
from tkinter import Toplevel
from tkinter import StringVar

class Cajero(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Cajero')
        self.geometry("300x200")
        self.pantalla = StringVar()

        self.create_widgets()
    
    def create_widgets(self):
        self.pantalla.set('pantalla cajero')
        lbl_title = ttk.Label(self, textvariable=self.pantalla, background='blue')
        lbl_title.pack()

        btnNumero1= ttk.Button(self, text='1',command=lambda:self.pantalla.set('selecciono 1'))
        btnNumero1.pack()
        
        btnNumero1= ttk.Button(self, text='2',command=lambda:self.pantalla.set('selecciono 2'))
        btnNumero1.pack()