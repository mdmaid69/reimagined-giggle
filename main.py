def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)