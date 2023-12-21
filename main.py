def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)