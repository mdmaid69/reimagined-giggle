import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities