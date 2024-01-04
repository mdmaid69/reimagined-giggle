import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import os
def list_files_in_directory(path):
        return os.listdir(path)