def sort_numbers(numbers):
        return sorted(numbers)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()