import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def find_unique_words(sentence):
        return set(sentence.split())