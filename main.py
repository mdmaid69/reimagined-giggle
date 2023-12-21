import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()