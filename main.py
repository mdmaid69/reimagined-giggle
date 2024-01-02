def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()