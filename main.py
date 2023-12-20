import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)