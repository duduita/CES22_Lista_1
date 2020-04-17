import turtle 

#criando objeto 
t = turtle.Turtle() 

def questao_2(n, l):  
    
    #para cada lado do polígono
    for i in range(n): 
        #andar l
        turtle.forward(l) 
        #girar o 'angulo interno"
        turtle.right(360 / n) 

questao_2(8, 50)
