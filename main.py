import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))