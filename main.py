import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def check_if_array_contains_item(array, item):
        return item in array