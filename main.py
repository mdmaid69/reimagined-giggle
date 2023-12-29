import array
def get_array_slice(array, i, j):
        return array[i:j]
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread