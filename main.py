def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True