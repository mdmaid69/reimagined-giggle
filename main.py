def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"