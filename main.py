import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())