# draw any polygon in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 

def draw_poly(n, l):  
    
    for _ in range(n): 
        turtle.forward(l) 
        turtle.right(360 / n) 

draw_poly(8, 50)
