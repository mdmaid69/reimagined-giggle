import array
def get_array_slice(array, i, j):
        return array[i:j]
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()