def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()