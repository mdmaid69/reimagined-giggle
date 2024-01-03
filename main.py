def sort_numbers(numbers):
        return sorted(numbers)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread