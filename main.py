import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())