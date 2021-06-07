# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_SISCLAPEEUAP.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect,
                          QAbstractAnimation, QTranslator, QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox,
                             QFrame, QLabel, QFileDialog )
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_framePrincipal(object):
    def setupUi(self, framePrincipal):
        framePrincipal.setObjectName("framePrincipal")
        framePrincipal.resize(866, 745)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        framePrincipal.setFont(font)
        self.groupBoxConfiguracion = QtWidgets.QGroupBox(framePrincipal)
        self.groupBoxConfiguracion.setGeometry(QtCore.QRect(40, 520, 171, 151))
        self.groupBoxConfiguracion.setObjectName("groupBoxConfiguracion")
        self.buttonCargarImagen = QtWidgets.QPushButton(self.groupBoxConfiguracion)
        self.buttonCargarImagen.setGeometry(QtCore.QRect(0, 20, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.buttonCargarImagen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/CargaImagen2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCargarImagen.setIcon(icon)
        self.buttonCargarImagen.setObjectName("buttonCargarImagen")
        self.buttonCargarModelo = QtWidgets.QPushButton(self.groupBoxConfiguracion)
        self.buttonCargarModelo.setGeometry(QtCore.QRect(0, 50, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.buttonCargarModelo.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/CargaModelo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCargarModelo.setIcon(icon1)
        self.buttonCargarModelo.setObjectName("buttonCargarModelo")
        self.buttonEliminar = QtWidgets.QPushButton(self.groupBoxConfiguracion)
        self.buttonEliminar.setGeometry(QtCore.QRect(0, 80, 101, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconos/Eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEliminar.setIcon(icon2)
        self.buttonEliminar.setObjectName("buttonEliminar")
        self.buttonEliminar_2 = QtWidgets.QPushButton(self.groupBoxConfiguracion)
        self.buttonEliminar_2.setGeometry(QtCore.QRect(170, 100, 101, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("iconos/Eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEliminar_2.setIcon(icon3)
        self.buttonEliminar_2.setObjectName("buttonEliminar_2")
        self.groupBoxClasificador = QtWidgets.QGroupBox(framePrincipal)
        self.groupBoxClasificador.setGeometry(QtCore.QRect(220, 520, 251, 151))
        self.groupBoxClasificador.setObjectName("groupBoxClasificador")
        self.buttomPredecir = QtWidgets.QPushButton(self.groupBoxClasificador)
        self.buttomPredecir.setGeometry(QtCore.QRect(30, 20, 191, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.buttomPredecir.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iconos/predecir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttomPredecir.setIcon(icon4)
        self.buttomPredecir.setObjectName("buttomPredecir")
        self.buttonAnterior = QtWidgets.QPushButton(self.groupBoxClasificador)
        self.buttonAnterior.setGeometry(QtCore.QRect(70, 80, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.buttonAnterior.setFont(font)
        self.buttonAnterior.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("iconos/izquierda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAnterior.setIcon(icon5)
        self.buttonAnterior.setObjectName("buttonAnterior")
        self.buttonSiguiente = QtWidgets.QPushButton(self.groupBoxClasificador)
        self.buttonSiguiente.setGeometry(QtCore.QRect(140, 80, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.buttonSiguiente.setFont(font)
        self.buttonSiguiente.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("iconos/derecha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSiguiente.setIcon(icon6)
        self.buttonSiguiente.setObjectName("buttonSiguiente")
        self.labelVersion = QtWidgets.QLabel(self.groupBoxClasificador)
        self.labelVersion.setGeometry(QtCore.QRect(20, 50, 221, 16))
        self.labelVersion.setText("")
        self.labelVersion.setObjectName("labelVersion")
        self.groupBoxIdentificacionpeces = QtWidgets.QGroupBox(framePrincipal)
        self.groupBoxIdentificacionpeces.setGeometry(QtCore.QRect(480, 520, 241, 151))
        self.groupBoxIdentificacionpeces.setObjectName("groupBoxIdentificacionpeces")
        self.labelPrediccion = QtWidgets.QLabel(self.groupBoxIdentificacionpeces)
        self.labelPrediccion.setGeometry(QtCore.QRect(20, 30, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelPrediccion.setFont(font)
        self.labelPrediccion.setObjectName("labelPrediccion")
        self.groupBoxSoftware = QtWidgets.QGroupBox(framePrincipal)
        self.groupBoxSoftware.setGeometry(QtCore.QRect(570, 670, 151, 41))
        self.groupBoxSoftware.setObjectName("groupBoxSoftware")
        self.labelNombreprograma = QtWidgets.QLabel(self.groupBoxSoftware)
        self.labelNombreprograma.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.labelNombreprograma.setObjectName("labelNombreprograma")
        self.labelNumeroVersion = QtWidgets.QLabel(self.groupBoxSoftware)
        self.labelNumeroVersion.setGeometry(QtCore.QRect(80, 20, 47, 13))
        self.labelNumeroVersion.setObjectName("labelNumeroVersion")
        self.comboBoxAcercade = QtWidgets.QComboBox(framePrincipal)
        self.comboBoxAcercade.setGeometry(QtCore.QRect(40, 680, 69, 22))
        self.comboBoxAcercade.setObjectName("comboBoxAcercade")
        self.comboBoxAcercade.addItem("")
        self.comboBoxAcercade.addItem("")
        self.comboBoxAcercade.addItem("")
        self.groupBoxImagen = QtWidgets.QGroupBox(framePrincipal)
        self.groupBoxImagen.setGeometry(QtCore.QRect(40, 0, 681, 521))
        self.groupBoxImagen.setObjectName("groupBoxImagen")
        self.frameContenedorImagen = QtWidgets.QFrame(self.groupBoxImagen)
        self.frameContenedorImagen.setGeometry(QtCore.QRect(10, 10, 662, 503))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frameContenedorImagen.setPalette(palette)
        self.frameContenedorImagen.setAutoFillBackground(True)
        self.frameContenedorImagen.setFrameShape(QtWidgets.QFrame.Box)
        self.frameContenedorImagen.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameContenedorImagen.setObjectName("frameContenedorImagen")
        self.labelImagen = QtWidgets.QLabel(self.frameContenedorImagen)
        self.labelImagen.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.labelImagen.setText("")
        self.labelImagen.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImagen.setObjectName("labelImagen")
        self.labelImagenUno = QtWidgets.QLabel(self.frameContenedorImagen)
        self.labelImagenUno.setGeometry(QtCore.QRect(-650, 0, 640, 480))
        self.labelImagenUno.setText("")
        self.labelImagenUno.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImagenUno.setObjectName("labelImagenUno")

        self.retranslateUi(framePrincipal)
        QtCore.QMetaObject.connectSlotsByName(framePrincipal)

    def retranslateUi(self, framePrincipal):
        _translate = QtCore.QCoreApplication.translate
        framePrincipal.setWindowTitle(_translate("framePrincipal", "Sistema para la clasificación de peces endemicos del Ecuador"))
        self.groupBoxConfiguracion.setTitle(_translate("framePrincipal", "Configuración"))
        self.buttonCargarImagen.setText(_translate("framePrincipal", "Cargar imagen"))
        self.buttonCargarModelo.setText(_translate("framePrincipal", "Cargar modelo"))
        self.buttonEliminar.setText(_translate("framePrincipal", "Eliminar imagen"))
        self.buttonEliminar_2.setText(_translate("framePrincipal", "Eliminar imagen"))
        self.groupBoxClasificador.setTitle(_translate("framePrincipal", "Clasificador"))
        self.buttomPredecir.setText(_translate("framePrincipal", "Predecir"))
        self.groupBoxIdentificacionpeces.setTitle(_translate("framePrincipal", "Identificación de peces"))
        self.labelPrediccion.setText(_translate("framePrincipal", "---> "))
        self.groupBoxSoftware.setTitle(_translate("framePrincipal", "Software"))
        self.labelNombreprograma.setText(_translate("framePrincipal", "SISCLAPEEUAP "))
        self.labelNumeroVersion.setText(_translate("framePrincipal", "V1.0"))
        self.comboBoxAcercade.setItemText(0, _translate("framePrincipal", "Acerca de"))
        self.comboBoxAcercade.setItemText(1, _translate("framePrincipal", "Creditos"))
        self.comboBoxAcercade.setItemText(2, _translate("framePrincipal", "Salir"))
        self.groupBoxImagen.setTitle(_translate("framePrincipal", "Imagen"))