import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def set_array_item(array, i, item):
        array[i] = item