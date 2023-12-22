import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread