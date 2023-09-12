import cv2
import face_recognition

# Inicializa a captura de vídeo da webcam (0 representa a webcam padrão)
cap = cv2.VideoCapture(0)

while True:
    # Captura um quadro de vídeo
    ret, frame = cap.read()

    # Encontra as localizações dos rostos no quadro
    face_locations = face_recognition.face_locations(frame)

    # Itera sobre as localizações dos rostos e desenha caixas delimitadoras
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Mostra o quadro com as caixas delimitadoras
    cv2.imshow("Captura de Rosto", frame)

    # Sai do loop quando a tecla 'q' é pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura de vídeo e fecha a janela
cap.release()
cv2.destroyAllWindows()
