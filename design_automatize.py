# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automatize_graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Digitador(object):
    def setupUi(self, Digitador):
        Digitador.setObjectName("Digitador")
        Digitador.setEnabled(True)
        Digitador.resize(682, 430)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        Digitador.setFont(font)
        Digitador.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(Digitador)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 220, 631, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.labelListFaltantes = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.labelListFaltantes.setFont(font)
        self.labelListFaltantes.setText("")
        self.labelListFaltantes.setObjectName("labelListFaltantes")
        self.gridLayout.addWidget(self.labelListFaltantes, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.arquivoFaltantes = QtWidgets.QLineEdit(self.centralwidget)
        self.arquivoFaltantes.setGeometry(QtCore.QRect(30, 30, 551, 20))
        self.arquivoFaltantes.setObjectName("arquivoFaltantes")
        self.arquivoEstoque = QtWidgets.QLineEdit(self.centralwidget)
        self.arquivoEstoque.setGeometry(QtCore.QRect(30, 90, 551, 20))
        self.arquivoEstoque.setObjectName("arquivoEstoque")
        self.inputAbrirFaltantes = QtWidgets.QPushButton(self.centralwidget)
        self.inputAbrirFaltantes.setGeometry(QtCore.QRect(590, 30, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.inputAbrirFaltantes.setFont(font)
        self.inputAbrirFaltantes.setObjectName("inputAbrirFaltantes")
        self.inputAbrirEstoque = QtWidgets.QPushButton(self.centralwidget)
        self.inputAbrirEstoque.setGeometry(QtCore.QRect(590, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.inputAbrirEstoque.setFont(font)
        self.inputAbrirEstoque.setObjectName("inputAbrirEstoque")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 200, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tituloFaltantes = QtWidgets.QLabel(self.centralwidget)
        self.tituloFaltantes.setGeometry(QtCore.QRect(30, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.tituloFaltantes.setFont(font)
        self.tituloFaltantes.setObjectName("tituloFaltantes")
        self.tituloEstoque = QtWidgets.QLabel(self.centralwidget)
        self.tituloEstoque.setGeometry(QtCore.QRect(30, 70, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.tituloEstoque.setFont(font)
        self.tituloEstoque.setObjectName("tituloEstoque")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(30, 132, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnRun.setFont(font)
        self.btnRun.setCheckable(False)
        self.btnRun.setObjectName("btnRun")
        Digitador.setCentralWidget(self.centralwidget)

        self.retranslateUi(Digitador)
        QtCore.QMetaObject.connectSlotsByName(Digitador)

    def retranslateUi(self, Digitador):
        _translate = QtCore.QCoreApplication.translate
        Digitador.setWindowTitle(_translate("Digitador", "DIGITAR NOTA"))
        self.inputAbrirFaltantes.setText(_translate("Digitador", "PushButton"))
        self.inputAbrirEstoque.setText(_translate("Digitador", "PushButton"))
        self.label.setText(_translate("Digitador", "Itens negativos no estoque DB (verificar e colocar similares):"))
        self.tituloFaltantes.setText(_translate("Digitador", "Arquivo .xlsx negativos MZTO"))
        self.tituloEstoque.setText(_translate("Digitador", "Arquivo .xlsx estoque DB"))
        self.btnRun.setText(_translate("Digitador", "DIGITAR"))