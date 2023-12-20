text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h