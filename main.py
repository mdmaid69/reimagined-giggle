def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import math
def calculate_permutations(n, k):
        return math.perm(n, k)