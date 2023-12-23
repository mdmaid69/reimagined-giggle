def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()