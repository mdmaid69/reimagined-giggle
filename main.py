import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())