def calculate_force(mass, acceleration):
        return mass * acceleration
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()