import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)