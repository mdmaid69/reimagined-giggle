import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import os
def get_file_size(filename):
        return os.path.getsize(filename)