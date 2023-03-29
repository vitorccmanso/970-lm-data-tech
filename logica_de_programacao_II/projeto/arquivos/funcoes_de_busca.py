from arquivos.manipulacao_json import *

def buscar_artista(nome_artista):
    return next((artista for artista in artistas["artistas"] if artista["nome"].lower() == nome_artista.lower()), None) 

def buscar_album(titulo_album, nome_artista):
    return next((album for album in albuns["albuns"] if album["titulo"].lower() == titulo_album.lower() and album["artista"].lower() == nome_artista.lower()), None) 

def buscar_musica(nome_musica, titulo_album):
    for album in albuns["albuns"]:
        if album["titulo"].lower() == titulo_album.lower():
            for musica in album["musicas"]:
                if musica["nome"].lower() == nome_musica.lower():
                    return musica

def buscar_playlist(nome_playlist):
    return next((playlist for playlist in playlists["playlists"] if playlist["nome_playlist"].lower() == nome_playlist.lower()), None)

#Utiliza a função 'buscar_playlist' para entregar ao usuário as informações da playlist buscada pelo nome
def buscar_nome_playlist(buscar_nome_playlist):
    playlist = buscar_playlist(buscar_nome_playlist)
    if playlist == None:
        print(f"A playlist '{buscar_nome_playlist}' não existe")
        return
    print(f"Infomações da playlist '{playlist['nome_playlist']}':")
    for musica in playlist["musicas"]:
        if musica == {}:
            print("Essa playlist não possui musicas")
        else:
            print(f"Musica: {musica['nome']}  Duração: {musica['tempo']}  Artista: {musica['artista']}\n----------------")

#Busca todas as playlists contendo a música digitada pelo usuário
def buscar_playlist_musica(musica_nome):
    print(f"Playlists contendo a música '{musica_nome}':")
    for playlist in playlists['playlists']:
        for musica in playlist['musicas']:
            if musica['nome'].lower() == musica_nome.lower():
                print(f"Playlist: {playlist['nome_playlist']}\nMúsicas: {playlist['musicas']}\n------------------------")

#Busca todas as playlists contendo o artista digitado pelo usuário
def buscar_playlist_artista(artista_nome):
    print(f"Playlists contendo o(a) artista '{artista_nome}':")
    for playlist in playlists['playlists']:
        for musica in playlist['musicas']:
            if musica['artista'].lower() == artista_nome.lower():
                print(f"Playlist: {playlist['nome_playlist']}\nMúsicas: {playlist['musicas']}\n------------------------")