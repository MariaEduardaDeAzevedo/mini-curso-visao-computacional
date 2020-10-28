import cv2 as cv
import numpy as np

# Classificador
'''
Este passo também pode ser realizado pegando os dados do arquivo formas.json, mas por fins de visualização, praticidade e tempo, utilizaremos um dicionário.
'''
forms = { 
  "3":"Triangulo", 
  "4":"Quadrilatero",
  "5":"Pentagono", 
  "6":"Hexagono",
  "7":"Heptagono", 
  "8":"Octogono",
  "9":"Eneagono", 
  "10":"Decagono",
  "11":"Undecagono", "12":"Dodecagono",
  "14":"Tetradecagono", "15":"Pentadecagono",
  "16":"Hexadecagono", "17":"Heptadecagono",
  "18":"Octodecagono", "19":"Eneadecagono",
  "20":"Icosagono", "30":"Triacontagono",
  "40":"Tetracontagono", "50":"Pentacontagono",
  "60":"Hexacontagono", "70":"Heptacontagono",
  "80":"Octacontagono", "90":"Eneacontagono",
  "100":"Hectagono"
}

# Lendo a imagem
image = cv.imread("arquivos/poligonos.jpg")

#PRÉ-PROCESSAMENTO
'''
Gradientes
Profundidade
'''
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_blur = cv.GaussianBlur(image_gray, (5,5), 1)
image_canny = cv.Canny(image_blur, 50, 50)

#LÓGICA
'''
'''

contours = cv.findContours(image_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]

for contour in contours:
	perimeter = cv.arcLength(contour, True)

	approx = cv.approxPolyDP(contour, perimeter*0.02, True)	

	vertex = len(approx)

	if vertex >= 3 and str(vertex) in forms.keys():
		
		name = forms[str(vertex)]

		x1, y1, x2, y2 = cv.boundingRect(approx)
		
		cv.rectangle(image, (x1, y1), (x1+x2, y1+y2), (255, 0, 255), thickness=2)

		cv.drawContours(image, contour, -1, (0, 255, 0), 1)		

		cv.putText(image, name, (x1+20, y1+10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))

# Saída
cv.imshow("Image", image)
cv.waitKey(0)

#BÔNUS - Detectando formas em VÍDEO (inclusive webcam!) 