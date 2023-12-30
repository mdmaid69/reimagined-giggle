import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))