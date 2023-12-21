import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)