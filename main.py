import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def convert_array_to_bytes(array):
        return array.tobytes()