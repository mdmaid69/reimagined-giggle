import math
def calculate_floor(x):
        return math.floor(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())