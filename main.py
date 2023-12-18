def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread