import random
def roll_die():
        return random.randint(1, 6)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True