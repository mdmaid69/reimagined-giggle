import array
def clear_array(array):
        array *= 0
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread