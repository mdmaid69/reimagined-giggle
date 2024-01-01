def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import math
def calculate_sign(x):
        return math.copysign(1, x)