text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)