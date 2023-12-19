import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())