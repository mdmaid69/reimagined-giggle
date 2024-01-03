def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()