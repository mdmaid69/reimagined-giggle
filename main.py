import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()