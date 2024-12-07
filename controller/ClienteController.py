from PyQt5 import QtWidgets, uic
from repository.ClienteRepository import ClienteRepository
from PyQt5.QtWidgets import QTableWidgetItem
from model.Cliente import Cliente

class ClienteController:
    def __init__(self):
        self.objClienteRepository = ClienteRepository()
        self.ventana = uic.loadUi("view/frmcliente.ui")
        self.ventana.tblclientes.cellClicked.connect(self.tblclientecellclick)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.listarClientes() 

    def btnguardarclick(self):
        Id_cliente = self.ventana.lblidcliente.text()
        nombre = self.ventana.txtnombre.text()
        apellido = self.ventana.txtapellido.text()
        telefono = self.ventana.txttelefono.text()
        nuevoCliente = Cliente(nombre, apellido, Id_cliente, telefono)
        if self.ventana.lblidcliente.isEnabled():
            self.objClienteRepository.insertarCliente(nuevoCliente)
        else:
            self.objClienteRepository.actualizarCliente(nuevoCliente)
        self.listarClientes()

    def tblclientecellclick(self, fila):
        Id_cliente = self.ventana.tblclientes.item(fila, 0).text()
        self.ventana.lblidcliente.setText(Id_cliente)
        self.ventana.lblidcliente.setEnabled(False)
        objCliente = self.objClienteRepository.obtenerClientexId(Id_cliente)
        self.ventana.txtnombre.setText(str(objCliente[1]))
        self.ventana.txtapellido.setText(str(objCliente[2]))
        self.ventana.txttelefono.setText(str(objCliente[3]))

    def listarClientes(self):
        listaClientes = self.objClienteRepository.listarClientes()
        cantidad = len(listaClientes)
        self.ventana.tblclientes.setRowCount(cantidad)
        fila = 0
        for cliente in listaClientes:
            self.ventana.tblclientes.setItem(fila, 0, QTableWidgetItem(str(cliente[0])))
            self.ventana.tblclientes.setItem(fila, 1, QTableWidgetItem(str(cliente[1])))
            self.ventana.tblclientes.setItem(fila, 2, QTableWidgetItem(str(cliente[2])))
            self.ventana.tblclientes.setItem(fila, 3, QTableWidgetItem(str(cliente[3])))
            fila +=1

