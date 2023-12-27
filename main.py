def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread