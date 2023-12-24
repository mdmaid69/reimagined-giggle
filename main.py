import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)