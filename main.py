import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())