import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()