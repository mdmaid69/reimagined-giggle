import array
def get_array_item_count(array, item):
        return array.count(item)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()