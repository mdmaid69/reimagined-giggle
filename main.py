import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import shutil
def delete_directory(path):
        shutil.rmtree(path)