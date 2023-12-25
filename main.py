def find_max(numbers):
        return max(numbers)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread