import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)