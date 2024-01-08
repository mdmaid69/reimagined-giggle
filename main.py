n = 10
print("Square numbers:", [x**2 for x in range(n)])
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()