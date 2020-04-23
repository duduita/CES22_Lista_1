def sum_of_initial_odds(lst):
    sum = 0
#verificando se tem a palavra 'sam'
    for i in range (len(lst)):
        if (lst[i] != 'sam'):
            sum = sum + 1
#se tiver 'sam' ele da break na função
        else: 
            break

    return sum

#exemplo da funcao funcionando
lst = ['auto', 'sam', 'tom']
print(sum_of_initial_odds(lst))