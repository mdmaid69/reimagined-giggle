import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()