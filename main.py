sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)