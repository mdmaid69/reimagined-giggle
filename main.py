text = "Hello, world!"
print("Reversed:", text[::-1])
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()