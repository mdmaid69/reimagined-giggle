import os
def change_working_directory(path):
        os.chdir(path)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()