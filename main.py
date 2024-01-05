text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))