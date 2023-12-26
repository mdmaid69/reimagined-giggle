import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}