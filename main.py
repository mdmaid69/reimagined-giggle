import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])