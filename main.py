import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h