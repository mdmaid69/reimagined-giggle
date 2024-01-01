import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def get_array_itemsize(array):
        return array.itemsize