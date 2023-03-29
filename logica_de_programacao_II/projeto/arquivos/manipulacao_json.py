import json

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

# -----Leitura dos arquivos json-----#
artistas = abrir_json("logica_de_programacao_II/projeto/arquivos/jsons/artistas.json")
albuns = abrir_json("logica_de_programacao_II/projeto/arquivos/jsons/albuns.json")
playlists = abrir_json("logica_de_programacao_II/projeto/arquivos/jsons/playlists.json")