import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)