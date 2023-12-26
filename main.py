import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())