import array
def convert_array_to_bytes(array):
        return array.tobytes()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()