  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)