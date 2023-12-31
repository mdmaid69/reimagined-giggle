text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)