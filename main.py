import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())