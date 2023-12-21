import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
n = 10
print("Powers of 2:", [2**x for x in range(n)])