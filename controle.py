from PyQt5 import uic, QtWidgets


def funcao_01():
    tela_servico.show()

def funcao_02():
    tela_gasto.show()


app = QtWidgets.QApplication([])
tela_principal = uic.loadUi("tela_principal.ui")
tela_servico = uic.loadUi("tela_serviço.ui")
tela_gasto = uic.loadUi("tela_gasto.ui")

tela_principal.pushButton.clicked.connect(funcao_01)
tela_principal.pushButton_2.clicked.connect(funcao_02)

tela_principal.show()
app.exec()
