import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def count_words(sentence):
        return len(sentence.split())