
def questao_4(lst):
    sum = 0
#verificando se o número é par - se não for, soma-se ao contador
    for i in lst:
        if i % 2 != 0:
            sum = sum + i
#se ele for par - break na função
        else: 
            break
    print(sum)
    return sum

questao_4(lst)

#se não tiver número par, ele vai resultar em 0.