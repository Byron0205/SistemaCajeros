from tkinter import ttk
from tkinter import Toplevel
from tkinter import StringVar
import tkinter as tk
from tkinter import*

class Cajero(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.title('Cajero')
        self.geometry("420x420")
        self.pantalla = StringVar() 
        self.create_widgets()
    
    def create_widgets(self):
        self.pantalla.set('pantalla cajero')
        
        frame_principal = ttk.Frame(self)
        frame_principal.pack(pady=100, fill=tk.BOTH, expand=True)

        frame_izquierdo = ttk.Frame(frame_principal)
        frame_izquierdo.pack(side=tk.LEFT, padx=10)

        frame_derecho = ttk.Frame(frame_principal)
        frame_derecho.pack(side=tk.RIGHT, padx=10)

        frame_central = ttk.Frame(frame_principal)
        frame_central.pack(fill=tk.BOTH, expand=True)

    

        lienzo = tk.Canvas(frame_central)
        lienzo.pack(fill=tk.BOTH, expand=True)



        # Obtener las dimensiones de la ventana
        ancho_ventana = self.winfo_width()
        alto_ventana = self.winfo_height()



        # Calcular las dimensiones del rectángulo
        ancho_rectangulo = 500
        alto_rectangulo = 500

        # Calcular las coordenadas para colocar el rectángulo en el centro
        x = (ancho_ventana - ancho_rectangulo) / 2 
        y = (alto_ventana - alto_rectangulo) / 4

        lienzo.create_rectangle(x, y, x + ancho_rectangulo, y + alto_rectangulo, fill="grey")



        # Botones de la lado izquierdo con los numeros
        btn_numero1 = ttk.Button(frame_izquierdo, text='50,000.00', command=lambda: self.pantalla.set('Seleccionaste 1'))
        btn_numero1.pack(pady=5, side=tk.TOP)
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