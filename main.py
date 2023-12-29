import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())