import array
def get_array_typecode(array):
        return array.typecode
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread