def calculate_roi(gain, cost):
        return (gain - cost) / cost
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()