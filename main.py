import math
def calculate_gamma_function(x):
        return math.gamma(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())