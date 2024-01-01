import array
def append_to_array(array, item):
        array.append(item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread