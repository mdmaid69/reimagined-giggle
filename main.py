import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time