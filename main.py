import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()