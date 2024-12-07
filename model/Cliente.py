from model.Persona import Persona

class Cliente(Persona):

    def __init__(self, _Nombre, _Apellido, _Id_cliente, _Telefono):
        super().__init__(_Nombre, _Apellido)
        self.Id_cliente = _Id_cliente
        self.Telefono = _Telefono