import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import array
def extend_array(array, iterable):
        array.extend(iterable)