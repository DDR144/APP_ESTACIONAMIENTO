from model.Persona import Persona

class Trabajador(Persona):

    def __init__(self, _Nombre, _Apellido, _Id_trabajador, _Turno):
        super().__init__(_Nombre, _Apellido,)
        self.Id_trabajador = _Id_trabajador
        self.Turno =_Turno