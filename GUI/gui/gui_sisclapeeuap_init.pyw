import sys
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from gui_sisclapeeuap import *


class GUIinit(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_framePrincipal()
        self.ui.setupUi(self)
        labelVersion = QLabel(self)
        labelVersion.setText(" SISCLAPEEUAP versión beta: 1.0  ")
        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(labelVersion, 0)
# ===================== CONECTAR SEÑALES =====================
        self.ui.buttonCargarImagen.clicked.connect(self.Cargar)
        self.ui.buttonEliminar.clicked.connect(self.Eliminar)
        self.ui.buttonAnterior.clicked.connect(self.anteriorSiguiente)
        self.ui.buttonSiguiente.clicked.connect(self.anteriorSiguiente)
        self.ui.buttonPredecir.clicked.connect(self.Predecir)
        # self.ui.buttonPredecir.clicked.connect(self.anteriorSiguiente)

# =============ESTABLECER VALORES PREDETERMINADO=========
        self.posicion = int
        self.estadoAnterior, self.estadoSiguiente = False, False
        self.carpetaActual = QDir()
        self.imagenesCarpeta = []
        #Parametros para cargar modelo entrenado de la CNN
        self.longitud, self.altura = 150, 150 #para estanderizar el tamano
        self.modelo = './modelo/modelo.h5' 
        self.pesos_modelo = './modelo/pesos.h5'
        self.cnn = load_model(self.modelo)  # Carga el modelo del directorio 
        self.cnn.load_weights(self.pesos_modelo) #Carga los pesos del modelo 
        
        #Parametros para bloquear funciones de cargar imagen y predecir imagen
        self.ui.buttonCargarModelo.setEnabled(False)
        self.ui.buttonPredecir.setEnabled(False) 
        self.ui.buttonEliminar.setEnabled(False)
        self.ui.buttonSiguiente.setEnabled(False)
        self.ui.buttonAnterior.setEnabled(False)
       
        

# ===============FUNCION DE BLOQUEAR BOTONES===========================

    def bloquearBotones(self, bool):
        self.ui.buttonCargarImagen.setEnabled(bool)
        self.ui.buttonEliminar.setEnabled(bool)
        self.ui.buttonAnterior.setEnabled(bool)
        self.ui.buttonSiguiente.setEnabled(bool)
        self.ui.buttonCargarModelo.setEnabled(bool)
        # self.ui.buttonPredecir.setEnabled(bool)
        # self.ui.buttonCargarModelo.setEnabled(bool)

# =================FUNCION MOSTRAR============================

    def Mostrar(self, label, imagen, nombre, posicionX=650):
       
        imagen = QPixmap.fromImage(imagen)

        # Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
        if imagen.width() > 640 or imagen.height() > 480:
            imagen = imagen.scaled(
                640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Mostrar imagen
        label.setPixmap(imagen)

        # Mostrar nombre en label

        # Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
        # y se desbloquean los botones).
        self.animacionMostar = QPropertyAnimation(label, b"geometry")
        self.animacionMostar.finished.connect(lambda: (self.statusBar.showMessage(nombre), self.ui.labelVersion.setText(nombre),
                                                       self.bloquearBotones(True)))
        self.animacionMostar.setDuration(200)
        self.animacionMostar.setStartValue(QRect(posicionX, 0, 640, 480))
        self.animacionMostar.setEndValue(QRect(0, 0, 640, 480))
        self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

# ===========================FUNCION LIMPIAR==========================

    def Limpiar(self, labelConImagen, labelMostrarImagen, imagen, nombre,
                posicionInternaX, posicionX=None):

        # Continuar
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


# ========================FUNCION ELIMINAR=====================================

    def Eliminar(self):
        def establecerValores():
            labelConImagen.clear()
            labelConImagen.move(0, 0)
            self.ui.labelVersion.setText("")
            

            # Limpiar la barra de estado
            self.statusBar.clearMessage()

            # Establecer los valores predeterminados
            self.posicion = int
            self.estadoAnterior, self.estadoSiguiente = False, False
            self.carpetaActual = QDir()
            self.imagenesCarpeta.clear()
            self.bloquearBotones(True)

        #Parametros para bloquear funciones de cargar imagen y predecir imagen
        self.ui.buttonCargarModelo.setEnabled(False)
        self.ui.buttonPredecir.setEnabled(False) 
        self.ui.buttonEliminar.setEnabled(False)
        self.ui.buttonSiguiente.setEnabled(False)
        self.ui.buttonAnterior.setEnabled(False)
        
        # Verificar que QLabel tiene imagen
        labelConImagen = ""
        if self.ui.labelImagen.pixmap():
            labelConImagen = self.ui.labelImagen
        elif self.ui.labelImagenUno.pixmap():
            labelConImagen = self.ui.labelImagenUno
        if labelConImagen:
            self.bloquearBotones(False)
            self.animacionEliminar = QPropertyAnimation(
                labelConImagen, b"geometry")
            self.animacionEliminar.finished.connect(establecerValores)
            self.animacionEliminar.setDuration(200)
            self.animacionEliminar.setStartValue(QRect(0, 0, 640, 480))
            self.animacionEliminar.setEndValue(QRect(-650, 0, 640, 480))
            self.animacionEliminar.start(QAbstractAnimation.DeleteWhenStopped)


# =============================FUNCION SIGUIENTE================================

    def anteriorSiguiente(self):
        if self.imagenesCarpeta:
            widget = self.sender().objectName()

            if widget == "Anterior":
                self.estadoAnterior = True if self.posicion == 0 else False
                self.estadoSiguiente = False

                self.posicion -= 1 if self.posicion > 0 else 0
                posicionInternaX, posicionX = 650, -650
            else:
                self.estadoSiguiente = True if self.posicion == len(
                    self.imagenesCarpeta)-1 else False
                self.estadoAnterior = False

                self.posicion += 1 if self.posicion < len(
                    self.imagenesCarpeta)-1 else 0
                posicionInternaX, posicionX = -650, 650

            if self.estadoAnterior or self.estadoSiguiente:
                return
            else:
                imagen = self.imagenesCarpeta[self.posicion]

                # Verificar que la carpeta que contiene la imagene exista
                if not QDir(self.carpetaActual).exists():
                    self.Eliminar()
                    return
                elif not QFile.exists(imagen):
                    # Obtener la ruta y el nombre de las imagenes que se encuentren en la
                    # carpeta de la imagen seleccionada
                    imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
                                                                QDir.Files, QDir.Name)

                    if not imagenes:
                        self.Eliminar()
                        return

                    self.imagenesCarpeta = [
                        imagen.absoluteFilePath() for imagen in imagenes]

                    self.posicion = randint(0, len(self.imagenesCarpeta)-1)
                    self.estadoAnterior = True if self.posicion == 0 else False
                    self.estadoSiguiente = True if self.posicion == len(
                        self.imagenesCarpeta)-1 else False
                elif QImage(imagen).isNull():
                    del self.imagenesCarpeta[self.posicion]

                    if not self.imagenesCarpeta:
                        self.Eliminar()
                        return

                    self.posicion = randint(0, len(self.imagenesCarpeta)-1)
                    self.estadoAnterior = True if self.posicion == 0 else False
                    self.estadoSiguiente = True if self.posicion == len(
                        self.imagenesCarpeta)-1 else False

                imagen = self.imagenesCarpeta[self.posicion]

                if self.ui.labelImagen.pixmap():
                    labelConImagen = self.ui.labelImagen
                elif self.ui.labelImagenUno.pixmap():
                    labelConImagen = self.ui.labelImagenUno

                # Función encargada de bloquear o desbloquear los botones
                self.bloquearBotones(False)

                # Nombre y extensión de la imagen
                nombre = QFileInfo(imagen).fileName()

                # Label en el que se va a mostrar la imagen
                labelMostrarImagen = self.ui.labelImagen if self.ui.labelImagenUno.pixmap(
                ) else self.ui.labelImagenUno

                # Quitar la imagen actual y mostrar la siguiente
                self.Limpiar(labelConImagen, labelMostrarImagen, QImage(imagen),
                             nombre, posicionInternaX, posicionX)


# ==================================FUNCION DE BOTON CARGAR===============================================
    def Cargar(self):

        #Activa los botones de las funcionalidades cargar modelo y predecir junto y pasar de imagen 
        self.ui.buttonCargarModelo.setEnabled(True)
        self.ui.buttonPredecir.setEnabled(True)
        self.ui.buttonSiguiente.setEnabled(True)
        self.ui.buttonAnterior.setEnabled(True)
        nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
                                                      QDir.currentPath(),
                                                      "Archivos de imagen (*.jpg *.png *.ico *.bmp)")

        if nombreImagen:
            # Verificar que QLabel tiene imagen
            labelConImagen = ""
            if self.ui.labelImagen.pixmap():
                labelConImagen = self.ui.labelImagen
            elif self.ui.labelImagenUno.pixmap():
                labelConImagen = self.ui.labelImagenUno

            imagen = QImage(nombreImagen)
            if imagen.isNull():
                if labelConImagen:
                    self.Eliminar()

                QMessageBox.information(self, "Visor de imágenes",
                                        "No se puede cargar %s." % nombreImagen)
                return

            # Obtener ruta de la carpeta que contiene la imagen seleccionada
            self.carpetaActual = QDir(
                QFileInfo(nombreImagen).absoluteDir().path())

            # Obtener la ruta y el nombre de las imagenes que se encuentren en la carpeta de
            # la imagen seleccionada
            imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
                                                        QDir.Files, QDir.Name)
            self.imagenesCarpeta = [imagen.absoluteFilePath()
                                    for imagen in imagenes]

            self.posicion = self.imagenesCarpeta.index(nombreImagen)
            self.estadoAnterior = True if self.posicion == 0 else False
            self.estadoSiguiente = True if self.posicion == len(
                self.imagenesCarpeta)-1 else False

            # Función encargada de bloquear o desbloquear los botones
            self.bloquearBotones(False)

            # Nombre y extensión de la imagen
            nombre = QFileInfo(nombreImagen).fileName()
            # self.ui.labelVersion.setText.str(nombre)

            if labelConImagen:
                posicionInternaX = -650
                labelMostrarImagen = self.ui.labelImagen if self.ui.labelImagenUno.pixmap(
                ) else self.ui.labelImagenUno
                self.Limpiar(labelConImagen, labelMostrarImagen,
                             imagen, nombre, posicionInternaX)
            else:
                self.Mostrar(self.ui.labelImagen, imagen, nombre)

# ==================Predecir========================================================
    def Predecir(self):
        self.Predict('Ancistrus (Fredy Nugra).jpg')


# =======================FUNCION BOTON PREDECIR=====================================

    def Predict(self, file):
        
        x = load_img(file, target_size=(self.longitud, self.altura))
        x = img_to_array(x)  # Convierte la imagen en un arreglo
        # Agrega una  dimensino al arreglo para procesar la informacion
        x = np.expand_dims(x, axis=0)
        # Dos dimenciones [1,0,0]LLama a la red para predicir la imagen
        array = self.cnn.predict(x)
        result = array[0]  # Dimension cero que contiene los nombres
        # Trae el indice del valor mas alto de resultado
        answer = np.argmax(result)
        if answer == 0:
            print("pred: bala")
        elif answer == 1:
            print("pred: Black-winged hatchetfish")
        elif answer == 2:
            print("pred: blood-red jewel cichild")
        elif answer == 3:
            print("pred: blue zebra angelfish")
        elif answer == 4:
            print("pred: bolivian ram")
        elif answer == 5:
            print("pred: botia striata fish")
        elif answer == 6:
            print("pred: Bristlenose_catfish")
        elif answer == 7:
            print("pred: celestial eye goldfish")
        elif answer == 8:
            print("pred: clown")
        elif answer == 9:
            print("pred: clown loach")
        elif answer == 10:
            print("pred: damsel fish")
        elif answer == 11:
            print("pred: Electric blue cichild")
        elif answer == 12:
            print("pred: Electric_fish")
        elif answer == 13:
            print("pred: figure eight puffer")
        elif answer == 14:
            print("pred: Flowerhorn cichlid")
        elif answer == 15:
            print("Gold")
        elif answer == 16:
            print("Guppy")
        elif answer == 17:
            print("lion")
        elif answer == 18:
            print("neon goby")
        elif answer == 19:
            print("neon tetra")
        elif answer == 20:
            print("Ocellate river stingray")
        elif answer == 21:
            print("Oscar Fish")
        elif answer == 22:
            print("Paradise Fish")
        elif answer == 23:
            print("Powder_blue_fish")
        elif answer == 24:
            print("Red_tail_black_shark")
        elif answer == 25:
            print("Sea Horse Fish")
        elif answer == 26:
            print("symphysodon discus")
        elif answer == 27:
            print("Thalassoma_bifasciatum")
        elif answer == 28:
            print("Yellow Tang")
        elif answer == 29:
            print("zebra danio fish")
        return answer


    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUIinit()
    myapp.show()
    sys.exit(app.exec_())
