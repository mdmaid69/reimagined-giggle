import array
def get_array_as_bytearray(array):
        return bytearray(array)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread