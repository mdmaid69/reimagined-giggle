import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])