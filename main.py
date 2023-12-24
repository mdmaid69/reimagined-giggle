import array
def set_array_item(array, i, item):
        array[i] = item
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()