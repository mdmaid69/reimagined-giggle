import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()