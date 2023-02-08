import sys
from design_automatize import *
from  PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class DesignImplement(QMainWindow, Ui_Digitador):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.inputAbrirFaltantes.clicked.connect(self.abrir_arquivo_faltantes)
    
    def abrir_arquivo_faltantes(self):
        table, _ = QFileDialog.getOpenFileName(None, 'Abrir arquivo'
        )
        self.inputAbrirFaltantes.setText(table)
        # self.table_file = 


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    run = DesignImplement()
    run.show()
    qt.exec_()