def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()