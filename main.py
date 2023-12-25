import array
def get_array_item(array, i):
        return array[i]
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread