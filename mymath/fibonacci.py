fibonacci_cache = {}

def fibonacci(n):
#memoization of values,  lru_cache from functools??cd
    if n in fibonacci_cache:
        return fibonacci_cache[n]
#compute nth value
    if n ==1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
#cache value
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(fibonacci(n))
