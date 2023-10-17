import os
import cv2
import face_recognition


pasta_referencia = "D:\\josea\\Fastech\\Projetos Python\\Reconhecimento facial\\meu_ambiente_virtual\\rostos_salvos"


imagens_referencia = [os.path.join(pasta_referencia, nome) for nome in os.listdir(pasta_referencia) if nome.lower().endswith(".jpg")]

# Carrega os rostos de referência
rostos_referencia = []
nomes_referencia = []

for imagem_referencia in imagens_referencia:
    nome = os.path.splitext(os.path.basename(imagem_referencia))[0]
    imagem_cv2 = cv2.imread(imagem_referencia)
    rosto_codificado = face_recognition.face_encodings(imagem_cv2)[0]  # Assume que há um único rosto na imagem
    rostos_referencia.append(rosto_codificado)
    nomes_referencia.append(nome)

# Limite de correspondência para considerar um rosto como compatível
limite_correspondencia = 0.4  


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    
    
    rostos_camera = face_recognition.face_locations(frame)
    codigos_camera = face_recognition.face_encodings(frame, rostos_camera)

    acesso_autorizado = False

    
    for codigo_camera, (top, right, bottom, left) in zip(codigos_camera, rostos_camera):
        comparacoes = face_recognition.face_distance(rostos_referencia, codigo_camera)
        nome_correspondente = "Desconhecido"  

        
        if len(comparacoes) > 0 and min(comparacoes) < limite_correspondencia:
            indice_correspondente = comparacoes.argmin()
            nome_correspondente = nomes_referencia[indice_correspondente]
            acesso_autorizado = True

        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        fonte = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nome_correspondente, (left + 6, bottom - 6), fonte, 0.5, (255, 255, 255), 1)

    
    cv2.imshow("Reconhecimento Facial", frame)

    
    if acesso_autorizado:
        print("Acesso Autorizado")
    else:
        print("Acesso Negado")

    # Para sair do loop pressione a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura de vídeo e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()