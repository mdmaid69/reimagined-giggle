import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def count_words(sentence):
        return len(sentence.split())