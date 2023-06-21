from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

# Manejo de hilos
from threading import Thread

from apps.login import Login

class BtnCajero(ttk.Frame):
    def __init__(self, parent, number, validar_cajero):
        super().__init__(parent)
        self.image = PhotoImage(file='cajero.png')
        self.number = number
        self.parent = parent
        self.Ocupado = False
        self.validar_cajero = validar_cajero

        self.create_widgets()

    def create_widgets(self):
        self.container_button1 = ttk.Frame(self)
        self.container_button1.grid(column=0, row=2)

        self.cajero1 = ttk.Button(self.container_button1, image=self.image, padding='8', command=self.OpenLogin)
        self.cajero1.pack(side='left')

        self.cajero1_label = ttk.Label(self.container_button1, text=f'Cajero {self.number}')
        self.cajero1_label.pack(side='left')

        self.cajero1.config(compound='left')

    def OpenLogin(self):
        """ if self.Ocupado:
            messagebox.showinfo('Cajero Ocupado', f'Cajero {self.number} esta ocupado.')
        else: """
        if not self.validar_cajero(self.number):
            self.Login()
        else:
            messagebox.showinfo('Cajero Ocupado', f'Cajero {self.number} esta ocupado.')


    def Login(self):
        login = Login(self.parent, self.number)
