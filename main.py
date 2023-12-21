import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}