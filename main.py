import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))