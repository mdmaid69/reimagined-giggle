import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())