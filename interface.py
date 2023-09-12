import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import face_recognition

def carregar_imagem():
    arquivo_imagem = filedialog.askopenfilename()

    if arquivo_imagem:
        imagem = face_recognition.load_image_file(arquivo_imagem)
        rosto_locations = face_recognition.face_locations(imagem)

        imagem_cv2 = cv2.imread("D:\josea\Fastech\Projetos Python\Reconhecimento facial\meu_ambiente_virtual\rostos_salvos")
                        
        for rosto_location in rosto_locations:
            top, right, bottom, left = rosto_location
            cv2.rectangle(imagem_cv2, (left, top), (right, bottom), (0, 255,0), 2)

        cv2.imshow("Reconhecimento Facial", imagem_cv2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



        resultado_label.config(text="Imagem carregada:\n" + arquivo_imagem)

    else:
        resultado_label.config(text="Nenhuma imagem selecionada") 


janela = tk.Tk()
janela.title("Reconhecimento Facial")


carregar_botao = tk.Button(janela, text="Carregar Imagem", command=carregar_imagem)
carregar_botao.pack(pady=10)


resultado_label = tk.Label(janela, text="", wraplength=300)
resultado_label.pack()



def capturar_rosto():
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Captura de Rosto", frame)

cap = cv2.VideoCapture(0)


janela = tk.Tk()
janela.title("Captura de Rosto")


botao_capturar = ttk.Button(janela, text="Capturar Rosto", command=capturar_rosto)
botao_capturar.pack(padx=20, pady=10)


def atualizar_interface():
    
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(frame_rgb)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    
    imagem_tk = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imagem_tk = Image.fromarray(imagem_tk)
    imagem_tk = ImageTk.PhotoImage(image=imagem_tk)
    label_imagem.config(image=imagem_tk)
    label_imagem.image = imagem_tk

    
    label_imagem.after(10, atualizar_interface)


label_imagem = ttk.Label(janela)
label_imagem.pack()


atualizar_interface()


janela.mainloop()


cap.release()
cv2.destroyAllWindows()

