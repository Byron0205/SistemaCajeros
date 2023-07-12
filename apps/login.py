from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox

#manejo hilos
from threading import Thread

from apps.cajero import Cajero

from baseDatos.funcionescajero import Actualizar_EstadoCajero

class Login(Toplevel):
    def __init__(self, root, num):
        super().__init__(root)
        self.title(f'Login Cajero {num}')
        self.geometry("300x200")
        self.number = num
        #para aplicar efecto de ocultar login
        self.parent =root

        self.inicio = False

        self.create_widgets()

        self.protocol("WM_DELETE_WINDOW", self.cerrarCajero)

    def cerrarCajero(self):
        Actualizar_EstadoCajero(0, self.number)
        self.destroy()


    def create_widgets(self):

        container = ttk.Frame(self)
        container.grid(column=0, row=0)

        # Configurar la alineación y el espaciado
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        lblUser = ttk.Label(container, text='usuario')
        lblUser.pack()
        
        txtUsuario = ttk.Entry(container)
        txtUsuario.pack()

        lblpassword = ttk.Label(container, text='contraseña')
        lblpassword.pack()
        
        txtpassword = ttk.Entry(container)
        txtpassword.pack()

        btnAceptar = ttk.Button(container, text="Iniciar sesion", command=lambda:self.validarLogin(user=txtUsuario.get(), password=txtpassword.get()))
        btnAceptar.pack()
        btnVolver = ttk.Button(container, text="Terminar", command=lambda:self.cerrarCajero(self.inicio))
        btnVolver.pack()

    def IniciarCajero(self):
        window_thread = Thread(target=self.VerCajero)
        window_thread.start()

    def VerCajero(self):
        cajero = Cajero(self.parent, self.number)

    def validarLogin(self,user, password):
        if user == 'admin' and password == 'admin':
            messagebox.showinfo(title='Inicio de sesion', message='Inicio de sesion exitoso!')
            self.inicio = True

            self.destroy()
            self.IniciarCajero()
        else:
            messagebox.showerror(title='Inicio de sesion', message='Credenciales incorrectas!')
            self.focus_force()