import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])