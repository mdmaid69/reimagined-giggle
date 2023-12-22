import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)