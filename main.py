import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def find_unique_words(sentence):
        return set(sentence.split())