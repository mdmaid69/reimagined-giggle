import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def find_unique_words(sentence):
        return set(sentence.split())