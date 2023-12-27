import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())