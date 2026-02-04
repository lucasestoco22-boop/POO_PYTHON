#função que verifica se é par
def par(a):
    par = (a % 2 == 0)
    return par
print(par(2))

#Para retornar se é par ou impar
def par_impar(a):
    if par(a):
        return "par"
    else:
        return "impar"
print(par_impar(5))

