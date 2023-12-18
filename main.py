import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)