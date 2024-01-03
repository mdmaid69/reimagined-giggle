import sys
def add_to_python_path(path):
        sys.path.append(path)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()