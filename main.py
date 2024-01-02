import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())