from turtle import *
#importando * de turtle

def questao_1(a,color,x,y):
    #tirando a caneta
    penup()
    #indo até o centro do quadro
    goto(x,y)
    setheading(90)
    backward(a//2)
    setheading(0)
    backward(a//2)
    #colocando a caneta
    pendown()
    pencolor(color)
    #para cada um dos (4) lados do quadros
    for _ in range(4):
        #andar a
        forward(a)
        #virar 90 graus
        left(90)

#chamando as funções para cada quadrado
questao_1(20,"pink",0,0)
questao_1(40,"pink",0,0)
questao_1(60,"pink",0,0)
questao_1(80,"pink",0,0)
questao_1(100,"pink",0,0)