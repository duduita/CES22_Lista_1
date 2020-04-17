#criando uma função inverse (nao entendi muito bem)
def reverse(s): 
    return s[::-1] 

def questao_9(s): 
    rev = reverse(s) 
  
    #Checando se a palavra é palindromo
    if (s == rev): 
        return print(True)
    return print(False)

questao_9('level')