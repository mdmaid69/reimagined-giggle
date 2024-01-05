import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array