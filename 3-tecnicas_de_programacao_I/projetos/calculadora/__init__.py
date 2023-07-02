from funcoes import *

def calcule():
    x = input("Digite um numero a: ")
    y = input("Digite um numero b: ")
    #Dicionário das opções válidas
    op_validas = {"soma": soma, "+": soma, "subtracao": sub, "-": sub, "divisao": div, "/": div, "multiplicacao": multi, "*": multi}
    op_input = input("Operações válidas: 'soma', 'subtracao', 'divisao', 'multiplicacao', '+', '-', '/', '*'\nDigite uma operação: ")
    #Verifica se a operação digitada existe no dicionário
    operacao = op_validas.get(op_input)
    if operacao:
        return(f"Resultado = {operacao(x, y)}")
    return("Operação inválida")
