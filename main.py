import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets