import time

def timer(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        result = func(*args, **kargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def example_function():
    pass

example_function()