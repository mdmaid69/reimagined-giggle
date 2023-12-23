import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()