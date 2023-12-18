def calculate_roi(gain, cost):
        return (gain - cost) / cost
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread