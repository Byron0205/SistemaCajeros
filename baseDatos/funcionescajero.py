import sqlite3
from datetime import datetime

def establecer_conexion():
    try:
        conexion = sqlite3.connect("baseDatos\cajeros.sqlite")
        return conexion
    except Exception as e:
        print(f'error al establecer la conexion {str(e)}')
        return None

def verificar_credenciales(num_tarjeta,contrsena):
    consulta = "Select IDusuario, numero_tarjeta from UsuarioxTarjeta where numero_tarjeta = ?  AND contrasena = ?"
    Parametros = (num_tarjeta,contrsena)
    conexion = establecer_conexion()
    if conexion is not None:
        cursor=conexion.cursor()    
        cursor.execute(consulta,Parametros)
        resultados = cursor.fetchall()
        conexion.close()
        # Verificar si hay resultados
        if resultados:
            # Obtener solo la lista de resultados
            idUsuario = resultados
            return idUsuario
        else:
            return []  # Devolver una lista vacía si no hay resultados
    else:
        print('error al establecer la conexion')

def Actualizar_Contrasena(contra,IDusuario):
    consulta = "UPDATE UsuarioxTarjeta set contrasena = ? WHERE IDusuario = ?"
    parametros= (contra,IDusuario)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def verificar_estadocajero(IDcajero:int):
    consulta = "Select estado from Cajeros where IDcajero = ?"
    Parametros = (IDcajero,)
    conexion = establecer_conexion()
    if conexion is not None:
        cursor=conexion.cursor()    
        cursor.execute(consulta,Parametros)
        resultados = cursor.fetchall()
        conexion.close()
        # Verificar si hay resultados
        if resultados:
            # Obtener solo la lista de resultados
            lista_resultados = [resultado[0] for resultado in resultados]
            return lista_resultados
        else:
            return []  # Devolver una lista vacía si no hay resultados
    else:
        print('error al establecer la conexion')

def Actualizar_EstadoCajero(Estado,IDcajero):
    consulta = "UPDATE Cajeros set estado = ? WHERE IDcajero = ?"
    parametros= (Estado,IDcajero,)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def registro_Movimiento(IDusuario,Monto,IDcajero,TipoMovimiento):
    Fecha = datetime.now()
    fechaFormato = Fecha.strftime('%d/%m/%y %H:%M:%S')
    consulta = "Insert into Movimientos(IDusuario,Monto,Fecha,IDcajero,IDtipoMovimiento) VALUES(?,?,?,?,?)"
    Parametros = (IDusuario,Monto,fechaFormato,IDcajero,TipoMovimiento)
    conexion = establecer_conexion()
    cursor=conexion.cursor()    
    cursor.execute(consulta,Parametros)
    conexion.commit()
    conexion.close()



def Ver_Saldo_Tajerta(IDusuario, num_tarjeta):
    consulta = "Select monto from UsuarioxTarjeta where IDusuario = ? and numero_tarjeta = ?"
    Parametros = (IDusuario, num_tarjeta)
    conexion = establecer_conexion()
    if conexion is not None:
        cursor=conexion.cursor()    
        cursor.execute(consulta,Parametros)
        resultados = cursor.fetchall()
        conexion.close()
        # Verificar si hay resultados
        if resultados:
            # Obtener solo la lista de resultados
            saldo_usuario = resultados[0]
            return saldo_usuario
        else:
            return []  # Devolver una lista vacía si no hay resultados
    else:
        print('error al establecer la conexion')

def Ver_Saldo_Usuario(IDusuario):
    consulta = "Select saldo from Usuarios where IDusuario = ?"
    Parametros = (IDusuario,)
    conexion = establecer_conexion()
    if conexion is not None:
        cursor=conexion.cursor()    
        cursor.execute(consulta,Parametros)
        resultados = cursor.fetchall()
        conexion.close()
        # Verificar si hay resultados
        if resultados:
            # Obtener solo la lista de resultados
            saldo_usuario = resultados[0]
            return saldo_usuario
        else:
            return []  # Devolver una lista vacía si no hay resultados
    else:
        print('error al establecer la conexion')

#Metodo para obtener el saldo los cajeros y usuarios
def ObtenerSaldo_Usuario_Cajero(IDcajero,IDusuario, num_tarjeta):
    consulta = "SELECT monto FROM cajeros WHERE IDcajero = ? UNION SELECT monto FROM UsuarioxTarjeta WHERE IDUsuario = ? and numero_tarjeta = ?"
    Parametros = (IDcajero,str(IDusuario),str(num_tarjeta))
    conexion = establecer_conexion()
    if conexion is not None:
        cursor=conexion.cursor()    
        cursor.execute(consulta,Parametros)
        resultados = cursor.fetchall()
        conexion.close()
        # Verificar si hay resultados
        if resultados:
            # Obtener solo la lista de resultados
            lista_resultados = [resultado[0] for resultado in resultados]
            return lista_resultados
        else:
            return []  # Devolver una lista vacía si no hay resultados
    else:
        print('error al establecer la conexion')

#valores= ObtenerSaldo_Usuario_Cajero(2,4,123)
#print(valores)

#metodo para guardar el saldo de la tarjeta del cliente
def insertar_saldoTarjetaCliente(monto,IDusuario, num_tarjeta):
    saldo= Ver_Saldo_Tajerta(IDusuario,num_tarjeta)
    FondosCuenta = int(monto) + saldo[0]
    consulta = "UPDATE UsuarioxTarjeta set monto  = ? WHERE IDusuario = ? and numero_tarjeta = ?"
    parametros= (FondosCuenta,IDusuario,num_tarjeta)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

#metodo para guardar el saldo total del cliente
def insertar_saldoCliente(monto,IDusuario):
    saldo= Ver_Saldo_Usuario(IDusuario)
    FondosCuenta = int(monto) + saldo[0]
    consulta = "UPDATE Usuarios set saldo  = ? WHERE IDusuario = ?"
    parametros= (FondosCuenta,IDusuario,)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def insertar_saldoCajero(monto,IDcajero):
    consulta = "UPDATE Cajeros set monto  = ? WHERE IDcajero = ?"
    parametros= (monto,IDcajero,)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def realizarRetiro(Monto, idUsuario,idCajero):
    conexion = establecer_conexion()
    #falta metodo para obtener saldos cajero y cuenta usuario

    SaldoRestanteUsuario = Monto
    SaldoRestanteCajero = Monto
    consultaUsuario = f'UPDATE Usuarios set saldo = ? where IDusuario=?'
    consultaCajero = f'UPDATE Cajeros set saldo = ? where IDcajero=?'
    ParametrosUsuario = (SaldoRestanteUsuario, idUsuario)
    ParametrosCajero = (SaldoRestanteCajero, idCajero)
    cursor= conexion.cursor()
    cursor.execute(consultaUsuario, ParametrosUsuario)
    cursor.execute(consultaCajero, ParametrosCajero)
    conexion.commit()
    conexion.close()