import os
import sys

#Montar o caminho para a pasta calculadora
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path)

#Executa o projeto
import calculadora
print(calculadora.calcule())