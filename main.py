import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)