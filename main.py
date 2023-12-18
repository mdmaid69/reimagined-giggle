import glob
def find_files(pattern):
        return glob.glob(pattern)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()