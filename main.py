import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def find_unique_words(sentence):
        return set(sentence.split())