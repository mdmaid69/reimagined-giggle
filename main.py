import math
def calculate_ceiling(x):
        return math.ceil(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())