import os
import shutil

# Defina a pasta que está bagunçada
pasta_alvo = r"C:\Users\jorge\Documentos"

regras = {
    "documentos": ["pdf", "docx", "txt"],
    "imagens": ["jpg", "jpeg", "png", "gif"],
    "videos": ["mp4", "avi", "mkv"],
    "musicas": ["mp3", "wav", "flac"],
    "planilhas": ["xlsx", "csv"]
}

for arquivo in os.listdir(pasta_alvo):

    caminho_arquivo = os.path.join(pasta_alvo, arquivo)

    # Ignora pastas
    if not os.path.isfile(caminho_arquivo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower().replace(".", "")

    for pasta, lista_extensoes in regras.items():

        if extensao in lista_extensoes:

            pasta_destino = os.path.join(pasta_alvo, pasta)

            os.makedirs(pasta_destino, exist_ok=True)

            shutil.move(
                caminho_arquivo,
                os.path.join(pasta_destino, arquivo)
            )

            break