def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print(factorial(5))
factorial_4 = print(factorial(4))
factorial_3 = print(factorial(3))
factorial_2 = print(factorial(2))
factorial_1 = print(factorial(1))
factorial_0 = print(factorial(0))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 3
print(fibonacci(number))