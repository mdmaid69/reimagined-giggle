import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])