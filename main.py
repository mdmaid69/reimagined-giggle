def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True