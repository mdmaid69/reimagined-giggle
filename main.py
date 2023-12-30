import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import sys
def print_python_version():
        print(sys.version)