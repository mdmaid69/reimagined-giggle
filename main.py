import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()