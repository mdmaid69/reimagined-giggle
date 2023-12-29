def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()