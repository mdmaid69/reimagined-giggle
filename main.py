def calculate_volume(length, width, height):
        return length * width * height
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)