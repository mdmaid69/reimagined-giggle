def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)