import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))