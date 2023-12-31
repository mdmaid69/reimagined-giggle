import math
def calculate_absolute_value(x):
        return math.fabs(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())