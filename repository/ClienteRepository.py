from util.ConexionBaseDatos import ConexionBaseDatos

class ClienteRepository:
    def __init__(self):
        self.conexion = ConexionBaseDatos().getConexion()

    def listarClientes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        return cursor.fetchall()

    def obtenerClientexId(self, Id_cliente):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM cliente WHERE Id_cliente = '{}'".format(Id_cliente)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCliente(self, cliente):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO cliente (nombre, apellido, telefono) VALUES ('{}', '{}', '{}')".format(cliente.Nombre, cliente.Apellido, cliente.Telefono)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarCliente(self, cliente):
        cursor = self.conexion.cursor()
        sql = "UPDATE cliente SET nombre = '{}', apellido = '{}', telefono = '{}' WHERE Id_cliente = '{}'".format(cliente.Nombre, cliente.Apellido, cliente.Telefono, cliente.Id_cliente)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
