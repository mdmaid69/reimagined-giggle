import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)