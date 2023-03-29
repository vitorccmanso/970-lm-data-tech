#Função soma
def soma(a, b):
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        raise TypeError("O input 'a' e 'b' devem ser numeros inteiros, ou decimais")

#Função subtração
def sub(a, b):
    try:
        return float(a) - float(b)
    except (ValueError, TypeError):
        raise TypeError("O input 'a' e 'b' devem ser numeros inteiros, ou decimais")
    
#Função divisão
def div(a, b):
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        raise TypeError("O input 'a' e 'b' devem ser numeros inteiros, ou decimais")
    if b != 0:
        return a / b
    return("0\nErro: Divisão inválida")

#Função multiplicação
def multi(a, b):
    try:
        return float(a) * float(b)
    except (ValueError, TypeError):
        raise TypeError("O input 'a' e 'b' devem ser numeros inteiros, ou decimais")


