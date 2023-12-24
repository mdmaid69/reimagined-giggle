import array
def get_array_buffer_info(array):
        return array.buffer_info()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread