def calculate_volume(length, width, height):
        return length * width * height
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)