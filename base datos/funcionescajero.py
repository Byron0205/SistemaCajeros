import sqlite3

def establecer_conexion():
    conexion = sqlite3.connect("cajeros.sqlite")
    return conexion

def verificar_credenciales(num_tarjeta,contrsena):
    consulta = "Select * from UsuarioxTarjeta where numero_tarjeta = ?  AND contrasena = ?"
    Parametros = (num_tarjeta,contrsena)
    conexion = establecer_conexion()
    cursor=conexion.cursor()    
    cursor.execute(consulta,Parametros)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def Actualizar_Contrasena(contra,IDusuario):
    consulta = "UPDATE UsuarioxTarjeta set contrasena = ? WHERE IDusuario = ?"
    parametros= (contra,IDusuario)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def verificar_estadocajero(IDcajero):
    consulta = "Select estado from Cajeros where IDcajero = ?"
    Parametros = (IDcajero)
    conexion = establecer_conexion()
    cursor=conexion.cursor()    
    cursor.execute(consulta,Parametros)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def Actualizar_EstadoCajero(Estado,IDcajero):
    consulta = "UPDATE Cajeros set estado = ? WHERE IDcajero = ?"
    parametros= (Estado,IDcajero)
    conexion = establecer_conexion()
    cursor=conexion.cursor() 
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def registro_Movimiento(IDusuario,Monto,Fecha,IDcajero,TipoMovimiento):
    consulta = "Insert into Movimientos(IDusuario,Monto,Fecha,IDcajero,IDtipoMovimiento VALUES(?,?,?,?,?)"
    Parametros = (IDusuario,Monto,Fecha,IDcajero,TipoMovimiento)
    conexion = establecer_conexion()
    cursor=conexion.cursor()    
    cursor.execute(consulta,Parametros)
    conexion.commit()
    conexion.close()