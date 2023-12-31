import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)