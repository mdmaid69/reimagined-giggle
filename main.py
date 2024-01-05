def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import random
def roll_die():
        return random.randint(1, 6)