import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)