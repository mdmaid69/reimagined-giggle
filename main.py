import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))