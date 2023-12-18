import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def count_words(sentence):
        return len(sentence.split())