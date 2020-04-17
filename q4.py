import random

def sum_of_initial_odds(lst):
    sum = 0
#test if element is odd number - if it's odd, add it to the previous integer
    for i in lst:
        if i % 2 != 0:
            sum = sum + i
#test if element is even number - if it's even, don't include it and break code
        else: 
            break

    return sum
