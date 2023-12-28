def count_words(sentence):
        return len(sentence.split())
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)