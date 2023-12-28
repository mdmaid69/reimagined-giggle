import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()