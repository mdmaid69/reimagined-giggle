import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)