def calculate_area(radius):
        return 3.14 * radius * radius
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()