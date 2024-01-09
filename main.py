import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time