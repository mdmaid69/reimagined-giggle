def add_numbers(a, b):
        return a + b
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread