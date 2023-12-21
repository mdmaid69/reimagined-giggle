import array
def reverse_array(array):
        array.reverse()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread