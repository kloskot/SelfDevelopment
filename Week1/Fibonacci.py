def fibonacci_itr(n):
    num1 = 1
    num2 = 1
    if(n < 2):
        return 1
    for _ in range(0,n-2):
        temp = num2
        num2 += num1
        num1 = temp
    return num2

def fibonacci_rec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)