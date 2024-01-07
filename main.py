def calculate_speed(distance, time):
        return distance / time
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h