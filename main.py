import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()