import cv2 as cv

VIDEO_1 = "video-1.mp4"
VIDEO_2 = "video-2.mp4"

FORMAS = { 
  3:"Triangulo", 4:"Quadrilatero", 5:"Pentagono", 
  6:"Hexagono", 7:"Heptagono", 
  8:"Octogono", 9:"Eneagono", 
  10:"Decagono", 11:"Undecagono", 12:"Dodecagono",
  14:"Tetradecagono", 15:"Pentadecagono",
  16:"Hexadecagono", 17:"Heptadecagono",
  18:"Octodecagono", 19:"Eneadecagono",
  20:"Icosagono", 30:"Triacontagono",
  40:"Tetracontagono", 50:"Pentacontagono",
  60:"Hexacontagono", 70:"Heptacontagono",
  80:"Octacontagono", 90:"Eneacontagono",
  100:"Hectagono"
}

def redimensionar(imagem):
    altura, largura, _ = frame.shape
    altura = altura - int((altura*0.8))
    largura = largura - int((largura*0.8))

    return cv.resize(frame, (largura, altura))


def processar(imagem):
    imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    imagem_desfocada = cv.blur(imagem_cinza, (2,2))
    imagem_canny = cv.Canny(imagem_desfocada, 70, 70)

    return imagem_canny

video = cv.VideoCapture(VIDEO_2)
rodando = True

while rodando:
    status, frame = video.read()

    if not status or cv.waitKey(1) & 0xff == ord('q'):
        rodando = False
    else:
        frame = redimensionar(frame)
        imagem_processada = processar(frame)

        contornos, _ = cv.findContours(imagem_processada, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        for contorno in contornos:
            perimetro = cv.arcLength(contorno, True)
            aproximacao = cv.approxPolyDP(contorno, perimetro * 0.02, True)
            vertices = len(aproximacao)

            area = cv.contourArea(contorno)

            if vertices >= 3 and vertices in FORMAS.keys() and area >= 100:
                x,y,w,h = cv.boundingRect(aproximacao)
                nome = FORMAS[vertices]
                cv.drawContours(frame, contorno, -1, (0,255,255), 2)
                cv.putText(frame, nome, (x+20, y+10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))

        cv.imshow("Video", frame)
