def factorial_itr(value):
    sum = 1
    if(value == 0 or value == 1):
        return sum
    while(value != 1):
        sum *= value
        value -= 1
    return sum

def factorial_rec(value):
    if(value == 1 or value == 0):
        return 1
    return value * factorial_rec(value - 1) 

