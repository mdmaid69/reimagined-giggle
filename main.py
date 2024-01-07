def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()