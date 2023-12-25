n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import random
def roll_die():
        return random.randint(1, 6)