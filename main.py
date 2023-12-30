import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def count_characters(sentence):
        return len(sentence)