import math
def calculate_error_function(x):
        return math.erf(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())