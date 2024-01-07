import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))