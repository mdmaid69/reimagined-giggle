import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)