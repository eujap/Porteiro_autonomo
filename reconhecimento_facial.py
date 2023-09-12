import face_recognition
import cv2

imagem = face_recognition.load_image_file("D:\josea\Fastech\Projetos Python\Reconhecimento facial\meu_ambiente_virtual\rostos_salvos")

rosto_locations = face_recognition.face_locations(imagem)

imagem_cv2 = cv2.imread("D:\josea\Fastech\Projetos Python\Reconhecimento facial\meu_ambiente_virtual\rostos_salvos")
                        
for rosto_location in rosto_locations:
    top, right, bottom, left = rosto_location
    cv2.rectangle(imagem_cv2, (left, top), (right, bottom), (0, 255,0), 2)

cv2.imshow("Reconhecimento Facial", imagem_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
