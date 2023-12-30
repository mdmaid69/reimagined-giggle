import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())