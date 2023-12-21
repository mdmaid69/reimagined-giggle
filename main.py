import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())