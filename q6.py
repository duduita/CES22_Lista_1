def questao_6(num):
#verificando que o número é maior do que 1
    if num > 1: 
        #sabe-se que se o número não for divisível por outro entre 2 e num/2, ele é primo
        for i in range(2, num//2): 
                
            if (num % i) == 0: 
                print(num, "is not a prime number") 
                break
        else: 
            print(num, "is a prime number") 
    
    else: 
        print(num, "is not a prime number") 

questao_6(20)