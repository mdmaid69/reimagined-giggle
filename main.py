import math
def calculate_factorial(n):
        return math.factorial(n)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())