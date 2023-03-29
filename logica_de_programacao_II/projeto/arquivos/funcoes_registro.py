from arquivos.funcoes_de_busca import *

#-----Funções que realizam as ações do aplicativo-----#

#Registra o artista, confere se ele existe a partir da funçao 'buscar_artista'
def registrar_artista():
    novo_artista = input("Digite o nome do artista: ")
    artista = buscar_artista(novo_artista)
    if artista == None:
        artistas["artistas"].append({"nome": novo_artista, "albuns": []})
        salvar_json("logica_de_programacao_II/projeto/arquivos/jsons/artistas.json", artistas)
        print(f"O artista '{novo_artista}' foi cadastrado com sucesso!")
        return
    print(f"O artista '{novo_artista}' já está cadastrado no app")

#Registra o album, confere se o artista existe e se o album existe
def registrar_album():
    artista_existente = input("Digite o nome do artista: ")
    artista = buscar_artista(artista_existente)
    if artista == None:
        print(f"O artista '{artista_existente}' ainda não está cadastrado no app")
        return
    index = artistas["artistas"].index(artista)
    nome_album = input("Digite o nome do album: ")
    album = buscar_album(nome_album, artista["nome"])
    if album != None:
        print(f"O album '{album['titulo']}' já existe")
        return
    qnt_musicas = input("Digite a quantidade de músicas no album: ")
    musicas = []
    for i in range(int(qnt_musicas)):
        nome_musica = input(f"Digite o nome da {i+1}° música: ")
        duracao_musica = input(f"Digite a duaração da {i+1}° música em 'mm:ss': ")
        musicas.append({"nome": nome_musica, "tempo": duracao_musica})
    add_album = {"titulo": nome_album, "artista": artista_existente, "musicas": musicas}
    artistas["artistas"][index]["albuns"].append(nome_album)
    salvar_json("logica_de_programacao_II/projeto/arquivos/jsons/artistas.json", artistas)
    albuns["albuns"].append(add_album)
    salvar_json("logica_de_programacao_II/projeto/arquivos/jsons/albuns.json", albuns)
    print(f"O album '{nome_album}' foi adicionado com sucesso!")

#Cria uma playlist caso ela nao exista, confere se a playlist existe pela função 'buscar playlist'
def criar_playlist():
    nome_usuario = input("Digite aqui seu nome: ")
    playlist = buscar_playlist(nome_usuario)
    if playlist != None:
        print(f"A playlist '{playlist['nome_playlist']}' já existe")
        return
    playlists["playlists"].append({"nome_playlist": nome_usuario, "musicas": []})
    salvar_json("logica_de_programacao_II/projeto/arquivos/jsons/playlists.json", playlists)
    add_musica(-1, nome_usuario)
    return

#Adiciona múscias para a playlist que está sendo criada até o usuário digitar 's' e confere se a música exsite no album pela função 'buscar_musica'
def add_musica(index, nome_usuario):
    while True:
        busca_artista = input("Artista: ")
        artista = buscar_artista(busca_artista)
        if artista == None:
            print("Artista não encontrado")
            continue
        busca_album = input("Album: ")
        album = buscar_album(busca_album, artista["nome"])
        if album == None:
            print("Album não encontrado")
            continue
        busca_musica = input("Musica: ")
        musica = buscar_musica(busca_musica, album["titulo"])
        if musica == None:
            print("Música não encontrada")
            continue
        musica = ({"nome": musica["nome"], "tempo": musica["tempo"], "artista": busca_artista})
        playlists["playlists"][index]["musicas"].append(musica)
        salvar_json("logica_de_programacao_II/projeto/arquivos/jsons/playlists.json", playlists)
        print(f"Música: {musica['nome']}\nDuração: {musica['tempo']}\nArtista: {busca_artista}")
        while True:
            escolha = input(f"Digite 's' para voltar ao menu de usuário ou 'a' para adicionar outra música na playlist '{nome_usuario}': ")
            if escolha.lower() == "s":
                return
            elif escolha.lower() != "a":
                print("Escolha inválida")
                continue
            else:
                break