import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
text = "Hello, world!"
print("Words:", len(text.split()))