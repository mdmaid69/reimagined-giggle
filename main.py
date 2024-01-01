import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)