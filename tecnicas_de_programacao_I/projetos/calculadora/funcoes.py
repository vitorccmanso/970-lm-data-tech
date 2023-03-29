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
