import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread