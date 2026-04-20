def cache(func):
    stored = {}
    def wrapper(*args, **kargs):
        if args in stored:
            print(f"从缓存中获取结果: f{args} = {stored[args]}")
            return stored[args]
        else:
            result = func(*args, **kargs)
            stored[args] = result
            print(f"计算结果并存储到缓存: f{args} = {result}")
            return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")