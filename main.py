import os
import shutil

download = os.path.join(os.path.expanduser("~"), "Downloads") #variável caminho da minha pasta de download


def organizar():
    os.chdir(download) #onde o código vai trabalhar
    lista = os.listdir()
    for bagunca in lista: #loop
        if os.path.isfile(bagunca): #verifica se a variável é um arquivo
            print(bagunca)
            name, exten = os.path.splitext(bagunca) #uma variável para nome e uma para extensão, splitext divide o nome da extensão
            #compactados
            if exten in (".zip", ".7z", ".rar", ".tar", ".gz"):
                shutil.move(os.path.join(download, bagunca,), os.path.join(download, "Compactados")) #move para suas pastas certas
                print(name, "foi movido para /Compactados.") #retorna uma mensagem falando para onde foi movido
            #imagens
            elif exten in (".jpg", ".png", ".jpeg", ".jpg" ".gif", ".webp", ".svg", ".bpm", ".tiff", ".raw", ".jfif", ".GIF", ".gif", "Gif",".JFIF"): 
                shutil.move(os.path.join(download, bagunca), os.path.join(download, "Imagens"))
                print(name, "Foi movido para /Imagens.")
            #arquivo de audio
            elif exten in (".mp3", ".aac", ".m4a", ".ogg",".flac",".alac", ".way", ".aiff"):
                shutil.move(os.path.join(download, bagunca), os.path.join(download, "Áudios")) 
                print(name, "foi movido para /Áudios.")
            #vídeos
            elif exten in (".mp4", ".mkv", ".mov", ".avi", ".mwv"):
                shutil.move(os.path.join(download, bagunca), os.path.join(download, "Vídeos"))
                print(name, "foi movido para /Vídeos")
            #executaveis
            elif exten == ".exe":
                shutil.move(os.path.join(download, bagunca), os.path.join(download, "Executáveis"))
                print(name, "foi movido para /Executáveis")
            #documentos
            elif exten in (".pdf",".docx",".doc", ".xlsx", ".pptx", ".txt", ".odt", ".rtf", ".psd"):
                shutil.move(os.path.join(download, bagunca), os.path.join(download, "Documentos"))
                print(name, "foi movido para /Documentos")
            #resto
            else: #se não se encaixar em nenhum dessas extensões ele n faz nada kkk
                print("Sinceramente eu não sei")

def verificacao(): 
    pastas = ["Vídeos", "Imagens", "Executáveis", "Documentos", "Compactados", "Áudios"] #lista com os nomes das pastas
    for diretorio in pastas: #loop
        if not os.path.exists(os.path.join(download, diretorio)): # if not, se não existir a pasta que está descrita vai pra próxima linha
            os.mkdir(os.path.join(download, diretorio)) #cria a pasta com o nome certo
            print("As pasta", diretorio, "foi criada.")
        else:
            print(diretorio, "já tinha.")

verificacao()
organizar()