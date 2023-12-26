def calculate_average(lst):
        return sum(lst) / len(lst)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()