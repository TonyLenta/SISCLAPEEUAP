from PyQt5.QtWidgets import QDialog
import sys
from gui_sisclapeeuap import *

class GUIinit(QtWidgets.QDialog): 
    def __init__(self, parent=None) :
        QtWidgets.QWidget.__init__(self, parent)
        self.ui =Ui_framePrincipal()
        self.ui.setupUi(self)
        
        




# ===================== CONECTAR SEÑALES =====================
        self.ui.buttonCargarImagen.clicked.connect(self.Cargar)
        self.ui.buttonEliminar.clicked.connect(self.Limpiar)


# Bloqueo de botones
    def bloquearBotones(self, bool):
        self.ui.buttonCargarImagen.setEnabled(bool)
        self.ui.buttonEliminar.setEnabled(bool)
      #  self.buttonAnterior.setEnabled(bool)
      #  self.buttonSiguiente.setEnabled(bool)

#Funcion Mostrar 
#Mostrar imagen  
    def Mostrar (self, label, imagen, nombre, posicionX=650):
        imagen = QPixmap.fromImage(imagen)

        # Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
        if imagen.width() > 640 or imagen.height() > 480:
            imagen = imagen.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Mostrar imagen
        label.setPixmap(imagen)

        # Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
        # y se desbloquean los botones).       
        self.animacionMostar = QPropertyAnimation(label, b"geometry")
        #self.animacionMostar.finished.connect(lambda: (self.parent.statusBar.showMessage(nombre),
        #                                               self.bloquearBotones(True)))
        self.animacionMostar.setDuration(200)
        self.animacionMostar.setStartValue(QRect(posicionX, 0, 640, 480))
        self.animacionMostar.setEndValue(QRect(0, 0, 640, 480))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

#Limpiar
    def Limpiar(self, labelConImagen, labelMostrarImagen, imagen, nombre,
                posicionInternaX, posicionX=None):

        #Continuar
        def Continuar(estado):
            if estado:
                if posicionX:
                    self.Mostrar(labelMostrarImagen, imagen, nombre, posicionX)
                else:
                    self.Mostrar(labelMostrarImagen, imagen, nombre)
            
        self.animacionLimpiar = QPropertyAnimation(labelConImagen, b"geometry")
        self.animacionLimpiar.finished.connect(lambda: labelConImagen.clear())
        self.animacionLimpiar.setDuration(200)
        # self.animacionLimpiar.valueChanged.connect(lambda x: print(x))
        self.animacionLimpiar.stateChanged.connect(Continuar)
        self.animacionLimpiar.setStartValue(QRect(0, 0, 640, 480))
        self.animacionLimpiar.setEndValue(QRect(posicionInternaX, 0, 640, 480))
        self.animacionLimpiar.start(QAbstractAnimation.DeleteWhenStopped)
        

#Boton cargar
    def Cargar(self):
        nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
                                                      QDir.currentPath(),
                                                      "Archivos de imagen (*.jpg *.png *.ico *.bmp)")

        if nombreImagen:
            # Verificar que QLabel tiene imagen
            labelConImagen = ""
            if self.ui.labelImagen.pixmap():
                labelConImagen = self.labelImagen
            elif self.ui.labelImagenUno.pixmap():
                labelConImagen = self.labelImagenUno
                
            imagen = QImage(nombreImagen)
            if imagen.isNull():
                if labelConImagen:
                    self.Eliminar()
                    
                QMessageBox.information(self, "Visor de imágenes",
                                        "No se puede cargar %s." % nombreImagen)
                return
            
            # Obtener ruta de la carpeta que contiene la imagen seleccionada
            self.carpetaActual = QDir(QFileInfo(nombreImagen).absoluteDir().path())

            # Obtener la ruta y el nombre de las imagenes que se encuentren en la carpeta de
            # la imagen seleccionada
            imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
                                                        QDir.Files, QDir.Name)
            self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

            self.posicion = self.imagenesCarpeta.index(nombreImagen)
            self.estadoAnterior = True if self.posicion == 0 else False
            self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False

            # Función encargada de bloquear o desbloquear los botones
            self.bloquearBotones(False)

            # Nombre y extensión de la imagen
            nombre = QFileInfo(nombreImagen).fileName()
            
            if labelConImagen:
                posicionInternaX = -650
                labelMostrarImagen = self.ui.labelImagen if self.ui.labelImagenUno.pixmap() else self.ui.labelImagenUno
                self.Limpiar(labelConImagen, labelMostrarImagen, imagen, nombre, posicionInternaX)
            else:
                self.Mostrar(self.ui.labelImagen, imagen, nombre)

        



if __name__== "__main__":
              app = QtWidgets.QApplication(sys.argv)
              myapp = GUIinit()
              myapp.show()
              sys.exit(app.exec_())
              
