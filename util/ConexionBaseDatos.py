import mysql.connector

class ConexionBaseDatos:
    def __init__(self):         
        self.conexion = mysql.connector.connect(host = 'localhost', database = 'bd_estacionamiento', user = 'root', password = 'didier')

    def getConexion(self):
        return self.conexion