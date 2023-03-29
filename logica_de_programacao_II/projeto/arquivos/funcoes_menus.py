from funcoes_registro import *
from funcoes_de_busca import *


#-----Funções dos menus-----#
def menu():
    while True:
        print("Você está no menu principal")
        print("1. Logar como administrador\n2. Logar como usuário\n3. Sair do aplicativo")
        opcao = input("Digite uma das opções acima: ")
        if opcao == "1":
            menu_admin()
        elif opcao == "2":
            menu_user()
        elif opcao == "3":
            print("Obrigado por utilizar o app!")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_admin():
    while True:
        print("Você está no menu de administrador")
        print("1. Registrar artista\n2. Registrar album\n3. Sair do menu de administrador")
        opcao_admin = input("Digite uma das opções acima: ")
        if opcao_admin == "1":
            registrar_artista()
        elif opcao_admin == "2":
            registrar_album()
        elif opcao_admin == "3":
            print("Você saiu do menu de administrador")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_user():
    while True:
        print("Você está no menu de usuário")
        print("1. Buscar playlist\n2. Criar playlist\n3. Sair do menu de usuário")
        opcao_user = input("Digite uma das opções acima: ")
        if opcao_user == "1":
            menu_busca_playlist()
        elif opcao_user == "2":
            criar_playlist()
        elif opcao_user == "3":
            print("Você saiu do menu de usuário")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_busca_playlist():
    while True:
        print("Vamos buscar a sua playlist!")
        print("1. Buscar por música\n2. Buscar por artista\n3. Buscar por nome\n4. Sair do menu de buscar playlist")
        opcao_busca_playlist = input("Digite uma das opções acima: ")
        if opcao_busca_playlist == "1":
            musica_nome = input("Digite o nome da múscia: ")
            buscar_playlist_musica(musica_nome)
        elif opcao_busca_playlist == "2":
            artista_nome = input("Digite o nome do artista: ")
            buscar_playlist_artista(artista_nome)
        elif opcao_busca_playlist == "3":
            nome_playlist = input("Digite o nome da playlist que deseja buscar: ")
            buscar_nome_playlist(nome_playlist)
        elif opcao_busca_playlist == "4":
            print("Você saiu do menu de buscar playlist")
            break
        else:
            print("Opção inválida, tente novamente.")

