import os
def remove_directory(path):
        os.rmdir(path)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()