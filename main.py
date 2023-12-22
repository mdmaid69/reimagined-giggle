import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())