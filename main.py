import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread