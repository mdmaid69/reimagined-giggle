import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets