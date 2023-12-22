import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)