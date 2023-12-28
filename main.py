import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])