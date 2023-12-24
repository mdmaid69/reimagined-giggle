import array
def get_array_as_bool(array):
        return bool(array)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()