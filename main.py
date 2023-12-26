import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])