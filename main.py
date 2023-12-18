def calculate_perpetuity(payment, rate):
        return payment / rate
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread