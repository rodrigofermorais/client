from PyQt5 import uic,QtWidgets

def funcao_01():  
    tela_projeto.show()

def funcao_02():  
    tela_manutencao.show()

def funcao_03():  
    tela_gasto.show()

def funcao_04():  
    tela_projeto.show()


app=QtWidgets.QApplication([])
tela_principal=uic.loadUi("tela_principal.ui")
tela_projeto=uic.loadUi("tela_projeto.ui")
tela_manutencao=uic.loadUi("tela_manutenção.ui")
tela_gasto=uic.loadUi("tela_gasto.ui")
tela_principal.pushButton.clicked.connect(funcao_01)
tela_principal.pushButton_2.clicked.connect(funcao_02)
tela_principal.pushButton_3.clicked.connect(funcao_03)




tela_principal.show()
app.exec()