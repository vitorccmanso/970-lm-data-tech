import json
import os

#-----Funções para ler e editar os arquivos json-----#
def abrir_json(arquivo):
    try:
        with open(arquivo, "r") as a:
            return json.load(a)
    except:
        return "O arquivo não existe"

def salvar_json(arquivo, dados):
    with open(arquivo, "w") as s:
        json.dump(dados, s)

# Obter o diretório atual de trabalho
dir_atual = os.path.dirname(os.path.abspath(__file__))
caminho_artistas = os.path.join(dir_atual, 'jsons', 'artistas.json')
caminho_albuns = os.path.join(dir_atual, 'jsons', 'albuns.json')
caminho_playlists = os.path.join(dir_atual, 'jsons', 'playlists.json')

# -----Leitura dos arquivos json-----#
artistas = abrir_json(caminho_artistas)
albuns = abrir_json(caminho_albuns)
playlists = abrir_json(caminho_playlists)

