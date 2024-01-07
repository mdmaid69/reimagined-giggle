import array
def remove_from_array(array, item):
        array.remove(item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread