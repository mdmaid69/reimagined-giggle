import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())