def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread