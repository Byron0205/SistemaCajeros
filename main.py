from tkinter import ttk, Tk

from components.btn_cajero import BtnCajero

from apps.cajero import Cajero


class GUI(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)


        root.title('Cajeros')
        root.geometry('400x450')

        self.create_widgets()


    def create_widgets(self):
        title= ttk.Label(self, text='Cabina cajeros', font='Arial 18')
        title.grid(column=0, row=1, columnspan=4)

        cajero1= BtnCajero(self,1)
        cajero1.grid(column=0,row=2)

        cajero2 = BtnCajero(self,2)
        cajero2.grid(column=0,row=3)
        
        cajero3 = BtnCajero(self,3)
        cajero3.grid(column=0,row=4)
        
        cajero4 =BtnCajero(self,4)
        cajero4.grid(column=0, row=5)

        btnCajero = ttk.Button(self, text='Cajero para revisar diseño', command=self.cajero)
        btnCajero.grid(column=0, row=6)

    def cajero(self):
        cajero = Cajero(self)

root = Tk()



#definir el frame y asignarselo a root
frame = GUI(root)
frame.grid(column=0, row=0)

#configuracion para centrarlo en pantalla
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

