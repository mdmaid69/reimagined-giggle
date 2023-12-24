import array
def convert_array_to_list(array):
        return array.tolist()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()