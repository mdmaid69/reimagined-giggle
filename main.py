import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread