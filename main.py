import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())