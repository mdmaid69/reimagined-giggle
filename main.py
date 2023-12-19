import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())