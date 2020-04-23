import cmath 

def questao_10(z, w):
    #pega parte real e parte imaginaria
    p = z.real + w.real
    q = z.imag + w.imag

    #transforma num complexo
    y = complex(p,q)
    print(y)


#Exemplo do código está funcionando:

a = (3+3j)
b = (2+3j)

#note que no input tem de haver a palavra 'complex'
questao_10(complex(a), complex(b))