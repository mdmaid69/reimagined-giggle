import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])