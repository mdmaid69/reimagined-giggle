import array
def get_array_as_list(array):
        return list(array)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread