import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()