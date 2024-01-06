def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)