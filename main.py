def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread