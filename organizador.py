import os

mapa_de_pastas = {
    "jpg": "Pictures",
    "png": "Pictures",
    "pdf": "Documents",
    "py": "Python",
    "docx": "Documents",
    "mp4": "Videos",
    "jpeg": "Picuteres"
    #adc as extensoes aqui!
}

entrada = str

while entrada != "nao" or "n": 

    pasta_origem = input("Digite a sua pasta a ser organizada: ")

    lista_de_arquivos = os.listdir(f"{pasta_origem}/")

    print(f"Arquivos encontrados: {lista_de_arquivos}")

    print("\nExtensoes: ")
    for extensoes in lista_de_arquivos:

        extensoes = extensoes.split('.')
        extensoes = extensoes[-1]
        print(extensoes)

    for nome_arquivo in lista_de_arquivos:
        
        partes = nome_arquivo.split('.')
        extensao = partes[-1]
        
        if '.' not in nome_arquivo:
            continue
        
        if extensao in mapa_de_pastas:
            pasta_destino = mapa_de_pastas[extensao]

            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)
                print(f"pasta '{pasta_destino}' criada!")

            caminho_origem = f"{pasta_origem}/{nome_arquivo}"
            caminho_destino = f"{pasta_destino}/{nome_arquivo}"

            os.rename(caminho_origem, caminho_destino)
            print(f"Arquivo '{nome_arquivo}' movido para '{pasta_destino}'")

        else:
            print(f"Extensão '{extensao}' do arquivo '{nome_arquivo}' não está no mapa, arquivo não movido.")

    print("\nOrganização concluída!")

    entrada = input("\nDeseja continuar organizando suas pastas?(s/n) ")
