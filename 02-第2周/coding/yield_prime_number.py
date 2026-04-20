def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def yield_prime_number():
    num = 2
    while True:
        if is_prime_number(num):
            yield num
        num += 1

def generate_prime_numbers(n):
    prime_gen = yield_prime_number()
    for _ in range(n):
        print(next(prime_gen),end = ' ')

generate_prime_numbers(100)