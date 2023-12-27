import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])