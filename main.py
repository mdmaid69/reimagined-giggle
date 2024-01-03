import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity