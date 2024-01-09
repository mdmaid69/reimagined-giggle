import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))