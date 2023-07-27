from tkinter import ttk
from tkinter import Toplevel
from tkinter import StringVar
import tkinter as tk
import time

from threading import Thread, Event

from baseDatos.funcionescajero import *


class Cajero(Toplevel):
    def __init__(self,root, num,idusuario, num_tarjeta):
        super().__init__(root)
        self.title('Cajero')
        self.geometry("420x420")
        self.number = num
        #codigo de tarjeta del usuario actual
        self.tarjeta = num_tarjeta
        #Id del usuario que ingreso al sistema
        self.idUsuario = idusuario
        #variable para saber si es deposito o retiro
        self.Tipo_Transaccion = None
        
        #varibles de cajero
        self.pantalla = StringVar()
        self.opcion = StringVar()
        self.monto = StringVar()
        self.mensaje = StringVar()
        
        self.create_widgets()

        #self.temporizador = None

        #variable validar operacion
        self.validarOperacion= False

        self.evento1= Event()
        self.evento2= Event()
        
        self.hilo = Thread(target=self.comprobarCuenta, args=(self.evento1, self.evento2,), daemon=True)

        self.hilo.start()

        self.protocol("WM_DELETE_WINDOW", lambda: self.cerrarCajero(0, self.number))

    def cerrarCajero(self, estado, num):
        Actualizar_EstadoCajero(estado, num)
        self.destroy()
    
    def create_widgets(self):
        Actualizar_EstadoCajero(1,self.number)
        self.pantalla.set('Seleccione una opcion...')
        
        frame_principal = ttk.Frame(self)
        frame_principal.pack(pady=100, fill=tk.BOTH, expand=True)

        frame_izquierdo = ttk.Frame(frame_principal)
        frame_izquierdo.pack(side=tk.LEFT, padx=10)

        frame_derecho = ttk.Frame(frame_principal)
        frame_derecho.pack(side=tk.RIGHT, padx=10)

        frame_central = ttk.Frame(frame_principal)
        frame_central.pack(fill=tk.BOTH, expand=True)

    
        lbl_pantalla = ttk.Label(frame_central, textvariable=self.pantalla, background='grey', foreground='white', font='Arial 12 bold')
        lbl_pantalla.pack(fill=tk.BOTH, expand=True)


        # Obtener las dimensiones de la ventana
        ancho_ventana = self.winfo_width()
        alto_ventana = self.winfo_height()


        # Calcular las dimensiones del rectángulo
        ancho_rectangulo = 500
        alto_rectangulo = 500

        # Calcular las coordenadas para colocar el rectángulo en el centro
        x = (ancho_ventana - ancho_rectangulo) / 2 
        y = (alto_ventana - alto_rectangulo) / 4

        # Botones de la lado izquierdo con los numeros
        btn_numero1 = ttk.Button(frame_izquierdo, text='50,000.00', command=lambda: self.monto1())
        btn_numero1.pack(pady=5, side=tk.TOP)
        btn_numero2 = ttk.Button(frame_izquierdo, text='30,000.00', command=lambda: self.monto2())
        btn_numero2.pack(pady=5)
        btn_numero3 = ttk.Button(frame_izquierdo, text='10,000.00', command=lambda: self.monto3())
        btn_numero3.pack(pady=5)

        # Botones de la lado derecho con los numeros
        btn_numero4 = ttk.Button(frame_derecho, text='Retiros', command=lambda: self.realizarRetiro())
        btn_numero4.pack(pady=5)
        btn_numero5 = ttk.Button(frame_derecho, text='Consultar', command=lambda: self.ConsultaMonto())
        btn_numero5.pack(pady=5)
        btn_numero6 = ttk.Button(frame_derecho, text='Depositos', command=lambda: self.realizarDeposito())
        btn_numero6.pack(pady=5)
        btn_numero7 = ttk.Button(frame_derecho, text='Salir', command=lambda: self.salir())
        btn_numero7.pack(pady=5)

    #limpiar pantalla al terminar transaccion
    def resetearPantalla(self):
        self.pantalla.set('Seleccione una opcion...')


    def salir(self):
        Actualizar_EstadoCajero(0,self.number)
        self.destroy()

    def tiempoEspera(self):
        if not self.validarOperacion:
            self.pantalla.set('Se acabo el tiempo de espera\nRetire la tarjeta')
            Actualizar_EstadoCajero(0,self.number)
            self.after(5000,self.destroy)


    def comprobarCuenta(self, evento1, evento2):
        while not evento2.is_set():
            print('inicio hilo')
            time.sleep(3)
        #    self.temporizador = self.after(10000, self.cerrarCajero,0, self.number)
            if self.monto.get() != '':
                mensajeUsuario = f'Transaccion exitosa\n'+ self.mensaje.get()
                self.pantalla.set(mensajeUsuario)
                self.after(5000,self.resetearPantalla)
                self.monto.set('')
            print('fin hilo')

    def realizarRetiro(self):
        #if self.temporizador is not None:
        #    self.after_cancel(self.temporizador)
        #    self.temporizador =None
        self.validarOperacion= False
        self.Tipo_Transaccion = "Retiro"
        self.opcion.set('Realizando retiro...\nIndique el monto:\n')
        self.pantalla.set(self.opcion.get())
        self.mensaje.set('retire su dinero')
        #tiempo de espera para realizar la operacion
        self.after(30000, self.tiempoEspera)
    
    def realizarDeposito(self):
        #if self.temporizador is not None:
        #    self.after_cancel(self.temporizador)
        #    self.temporizador =None
        self.validarOperacion= False
        self.Tipo_Transaccion = "Deposito"
        self.opcion.set('Realizando deposito...\nIndique el monto:\n')
        #mensaje para el tipo de transaccion
        self.mensaje.set('dinero agregado a su cuenta.')
        self.pantalla.set(self.opcion.get())

        #tiempo de espera para realizar la operacion
        self.after(30000, self.tiempoEspera)

    #Metodo para la consulta de los montos
    def ConsultaMonto(self):
        saldo_Usuario = Ver_Saldo_Tajerta(self.idUsuario,self.tarjeta)
        saldo_Usuario = saldo_Usuario[0]
        mensaje = f"Su saldo es de ${saldo_Usuario}"
        registro_Movimiento(self.idUsuario,0,self.number,3)
        self.pantalla.set(mensaje)

    def monto1(self):
        #if self.temporizador is not None:
        #    self.after_cancel(self.temporizador)
        #    self.temporizador =None
        self.monto.set('50000')
        self.pantalla.set(self.opcion.get()+self.monto.get())
        
        self.validarOperacion = True

        #cancelar tiempo espera si se ingresa un monto
        self.after_cancel(self.tiempoEspera)

        #Validaciones
        resultado = ObtenerSaldo_Usuario_Cajero(self.number,self.idUsuario, self.tarjeta)
        saldo_cajero = resultado[1]
        saldo_Usuario = resultado[0]
        print('ver tarjeta desde cajero: ', self.tarjeta)
        if(self.Tipo_Transaccion == "Deposito"):
            #Revisar si pasa un entero o string
            if(saldo_cajero>=50000):
                insertar_saldoCliente(self.monto.get(),self.idUsuario)
                insertar_saldoTarjetaCliente(self.monto.get(),self.idUsuario, self.tarjeta)
                registro_Movimiento(self.idUsuario,self.monto.get(),self.number,1)
                pass
            else:
                mensaje = "El cajero no cuenta con esa cantidad para realizar el deposito"
                self.pantalla.set(mensaje)
                pass
        if(self.Tipo_Transaccion == "Retiro"):
            if(saldo_cajero>=50000 ):
                if(saldo_Usuario>=50000):
                    retirar_saldoCliente(self.monto.get(),self.idUsuario)
                    retirar_saldoTarjetaCliente(self.monto.get(),self.idUsuario,self.tarjeta)
                    modificar_saldoCajero(self.monto.get(), self.number)
                    registro_Movimiento(self.idUsuario,self.monto.get(),self.number,2)
                    pass
                else:
                    mensaje = "Su cuenta bancaria no cuenta con los suficientes fondos"
                    self.pantalla.set(mensaje)
            else:
                mensaje = "El cajero no cuenta con los suficientes fondos"
                self.pantalla.set(mensaje)
        #iniciar el proceso de comprobacion de fondos
        self.after(3000, self.evento1.set)
    
    def monto2(self):
        #if self.temporizador is not None:
        #    self.after_cancel(self.temporizador)
        #    self.temporizador =None
        self.monto.set('30000')
        self.pantalla.set(self.opcion.get()+self.monto.get())
        

        #Validaciones
        resultado = ObtenerSaldo_Usuario_Cajero(self.number,self.idUsuario,self.tarjeta)
        saldo_cajero = resultado[1]
        saldo_Usuario = resultado[0]
        if(self.Tipo_Transaccion == "Deposito"):
            #Revisar si pasa un entero o string
            if(saldo_cajero>=30000):
                insertar_saldoCliente(self.monto.get(),self.idUsuario)
                insertar_saldoTarjetaCliente(self.monto.get(),self.idUsuario, self.tarjeta)
                registro_Movimiento(self.idUsuario,self.monto.get(),self.number,1)
            else:
                mensaje = "El cajero no cuenta con esa cantidad para realizar el deposito"
                self.pantalla.set(mensaje)
                pass
        if(self.Tipo_Transaccion == "Retiro"):
            if(saldo_cajero>=30000 ):
                if(saldo_Usuario>=30000):
                    retirar_saldoCliente(self.monto.get(),self.idUsuario)
                    retirar_saldoTarjetaCliente(self.monto.get(),self.idUsuario,self.tarjeta)
                    modificar_saldoCajero(self.monto.get(), self.number)
                    registro_Movimiento(self.idUsuario,self.monto.get(),self.number,2)
                else:
                    mensaje = "Su cuenta bancaria no cuenta con los suficientes montos"
                    self.pantalla.set(mensaje)
            else:
                mensaje = "El cajero no cuenta con los suficientes montos"
                self.pantalla.set(mensaje)

        self.after(3000, self.evento1.set)
    
    def monto3(self):
        #if self.temporizador is not None:
        #    self.after_cancel(self.temporizador)
        #    self.temporizador =None
        self.monto.set('10000')
        self.pantalla.set(self.opcion.get()+self.monto.get())
        
        #Validaciones
        resultado = ObtenerSaldo_Usuario_Cajero(self.number,self.idUsuario, self.tarjeta)
        print(resultado)
        saldo_Usuario = resultado[0]
        saldo_cajero = resultado[1]
        if(self.Tipo_Transaccion == "Deposito"):
            #Revisar si pasa un entero o string
            if(saldo_cajero>=10000):
                insertar_saldoCliente(self.monto.get(),self.idUsuario)
                insertar_saldoTarjetaCliente(self.monto.get(),self.idUsuario, self.tarjeta)
                registro_Movimiento(self.idUsuario,self.monto.get(),self.number,1)
            else:
                mensaje = "El cajero no cuenta con esa cantidad para realizar el deposito"
                self.pantalla.set(mensaje)
                pass
        if(self.Tipo_Transaccion == "Retiro"):
            if(saldo_cajero>=10000 ):
                if(saldo_Usuario>=10000):
                    retirar_saldoCliente(self.monto.get(),self.idUsuario)
                    retirar_saldoTarjetaCliente(self.monto.get(),self.idUsuario,self.tarjeta)
                    modificar_saldoCajero(self.monto.get(), self.number)
                    registro_Movimiento(self.idUsuario,self.monto.get(),self.number,2)
                else:
                    mensaje = "Su cuenta bancaria no cuenta con los suficientes montos"
                    self.pantalla.set(mensaje)
            else:
                mensaje = "El cajero no cuenta con los suficientes montos"
                self.pantalla.set(mensaje)

                
        self.after(3000, self.evento1.set)

