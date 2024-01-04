import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))