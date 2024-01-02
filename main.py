import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())