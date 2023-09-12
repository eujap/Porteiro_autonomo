import os
import uuid

diretorio_de_armazenamento = "rostos_salvos"

def salvar_imagem(imagem):
    nome_arquivo = str(uuid.uuid4()) + ".jpg"
    diretorio = os.path.join(diretorio_de_armazenamento, nome_arquivo)

    if not os.path.exists(diretorio_de_armazenamento):
        os.makedirs(diretorio_de_armazenamento)

    with open(diretorio, "wb") as arquivo:
        arquivo.write(imagem)

    return nome_arquivo


def buscar_imagem(nome_arquivo):
    diretorio = os.path.join(diretorio_de_armazenamento, nome_arquivo)
    if os.path.exists(diretorio):

        with open(diretorio, "rb") as arquivo:
            return arquivo.read()
    else:
        return None
    

def listar_imagens():
    imagens = []
    if os.path.exists(diretorio_de_armazenamento):
        for nome_arquivo in os.listdir(diretorio_de_armazenamento):
            imagens.append(nome_arquivo)

    return imagens