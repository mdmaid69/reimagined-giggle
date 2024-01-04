text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)