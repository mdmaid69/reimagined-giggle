import array
def get_array_index(array, item):
        return array.index(item)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()