def questao_7(lst):
    sum = 0
#varrendo a lista e para cada elemento da lista soma-se o seu respectivo quadrado
    for i in range (len(lst)):
            sum = sum + lst[i]*lst[i]
    print(sum)
    return sum

lst = [1, 2, 3]
questao_7(lst)