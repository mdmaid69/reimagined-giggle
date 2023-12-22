import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()