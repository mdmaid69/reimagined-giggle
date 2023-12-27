import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps