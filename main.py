import array
def get_bytes_from_array(array):
        return array.tobytes()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()