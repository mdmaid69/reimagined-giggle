def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()