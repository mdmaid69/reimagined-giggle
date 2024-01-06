import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()