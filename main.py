import array
def extend_array(array, iterable):
        array.extend(iterable)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread