from PyQt5 import QtWidgets, uic
from controller.ClienteController import ClienteController

class PrincipalController:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/menuprincipal.ui")
        self.ventana.show()
        # self.ventana.btningreso.clicked.connect(self.btningresoOnClick)
        self.ventana.actionCliente.triggered.connect(self.actionClienteClick)
        app.exec()

    def actionClienteClick(self):
        self.frmcliente = ClienteController()
        self.frmcliente.ventana.show()

    # def btningresoOnClick(self):
    #     self.form = ClienteController()
    #     self.form.ventana.show()