import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()