def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)