def fibo_1(n):
    if n <= 1:
        return n
    return fibo_1(n - 1) + fibo_1(n - 2)
    
print(fibo_1(6))



def fibo(n):
    cache = {0:0, 1:1}
    def fibonacci(n):
        if n not in cache:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci(n)


print(fibo(6))