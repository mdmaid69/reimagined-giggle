def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread