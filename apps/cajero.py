from tkinter import ttk
from tkinter import Toplevel
from tkinter import StringVar
import tkinter as tk

class Cajero(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Cajero')
        self.geometry("300x200")
        self.pantalla = StringVar()

        self.create_widgets()
    
    def create_widgets(self):
        self.pantalla.set('pantalla cajero')
        
        frame_principal = ttk.Frame(self)
        frame_principal.pack(pady=20, fill=tk.BOTH, expand=True)

        frame_izquierdo = ttk.Frame(frame_principal)
        frame_izquierdo.pack(side=tk.LEFT, padx=10)

        frame_derecho = ttk.Frame(frame_principal)
        frame_derecho.pack(side=tk.RIGHT, padx=10)

        lbl_pantalla = ttk.Label(frame_principal, textvariable=self.pantalla, background='blue')
        lbl_pantalla.pack()
        # Botones de la lado izquierdo con los numeros
        btn_numero1 = ttk.Button(frame_izquierdo, text='50,000.00', command=lambda: self.pantalla.set('Seleccionaste 1'))
        btn_numero1.pack(pady=5)
        btn_numero2 = ttk.Button(frame_izquierdo, text='30,000.00', command=lambda: self.pantalla.set('Seleccionaste 1'))
        btn_numero2.pack(pady=5)
        btn_numero3 = ttk.Button(frame_izquierdo, text='10,000.00', command=lambda: self.pantalla.set('Seleccionaste 1'))
        btn_numero3.pack(pady=5)
        # Botones de la lado derecho con los numeros
        btn_numero4 = ttk.Button(frame_derecho, text='Retiros', command=lambda: self.pantalla.set('Seleccionaste 2'))
        btn_numero4.pack(pady=5)
        btn_numero5 = ttk.Button(frame_derecho, text='Consultar', command=lambda: self.pantalla.set('Seleccionaste 2'))
        btn_numero5.pack(pady=5)
        btn_numero6 = ttk.Button(frame_derecho, text='Depositos', command=lambda: self.pantalla.set('Seleccionaste 2'))
        btn_numero6.pack(pady=5)

