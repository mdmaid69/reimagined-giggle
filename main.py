import math
def calculate_combinations(n, k):
        return math.comb(n, k)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())