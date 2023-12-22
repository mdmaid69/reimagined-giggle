import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h