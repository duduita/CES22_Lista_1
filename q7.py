def sum_of_initial_odds(lst):
    sum = 0
#test if element is odd number - if it's odd, add it to the previous integer
    for i in range (len(lst)):
            sum = sum + lst[i]*lst[i]
    return sum

lst = [1, 2, 3]
print(sum_of_initial_odds(lst))