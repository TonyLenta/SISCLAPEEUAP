#Procesa las imagenes para identificar las clses
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 150, 150 #para estanderizar el tamano
modelo = './modelo/modelo.h5' 
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)  # Carga el modelo del directorio 
cnn.load_weights(pesos_modelo) #Carga los pesos del modelo 

#Funcion para identificar el animal devolviendo su nombre
def predict(file):
  x = load_img(file, target_size=(longitud, altura)) #Carga imagen
  x = img_to_array(x) # Convierte la imagen en un arreglo
  x = np.expand_dims(x, axis=0) #Agrega una  dimensino al arreglo para procesar la informacion
  array = cnn.predict(x) #Dos dimenciones [1,0,0]LLama a la red para predicir la imagen
  result = array[0] #Dimension cero que contiene los nombres
  answer = np.argmax(result) #Trae el indice del valor mas alto de resultado
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


predict('Ancistrus (Fredy Nugra).jpg')