import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))