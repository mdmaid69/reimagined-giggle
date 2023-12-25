import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal