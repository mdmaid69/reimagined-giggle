import array
def get_array_buffer_info(array):
        return array.buffer_info()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()