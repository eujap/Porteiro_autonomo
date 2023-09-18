import cv2
import dlib
import os


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # baixar o arquivo
 

referencia_image_path = "D:\josea\Fastech\Projetos Python\Reconhecimento facial\meu_ambiente_virtual\rostos_salvos"

if not os.path.exists(referencia_image_path):
    print(f"Arquivo de referência não encontrado em: {referencia_image_path}")
    exit()


reference_image = cv2.imread("reference_face.jpg")


def compare_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = detector(gray_frame)

    for face in faces:
        landmarks = predictor(gray_frame, face)

        
        reference_landmarks = predictor(gray_frame, face)

        
        diff = cv2.absdiff(reference_image, reference_landmarks)

        
        similarity_threshold = 10000  # Ajuste conforme necessário

        
        total_diff = diff.sum()

        if total_diff < similarity_threshold:
            return True

    return False


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if compare_faces(frame):
        print("Acesso permitido")
        break

    cv2.imshow("Comparação de Rostos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
