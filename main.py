import array
def remove_from_array(array, item):
        array.remove(item)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()