def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()