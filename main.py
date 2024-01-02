import math
def calculate_circle_area(radius):
        return math.pi * radius**2
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())