def find_unique_words(sentence):
        return set(sentence.split())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)