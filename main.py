import math
def calculate_exponential(x):
        return math.exp(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())