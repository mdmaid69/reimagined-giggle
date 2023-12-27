import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True