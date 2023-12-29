import array
def get_list_from_array(array):
        return array.tolist()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()