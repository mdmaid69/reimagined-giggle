import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)