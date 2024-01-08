import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())