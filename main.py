import math
def calculate_cosine(x):
        return math.cos(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())