import array
def get_bytes_from_array(array):
        return array.tobytes()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread