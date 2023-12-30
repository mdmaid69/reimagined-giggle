import math
def calculate_arc_cosine(x):
        return math.acos(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())