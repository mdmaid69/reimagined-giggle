import array
def get_array_as_complex(array):
        return complex(array[0])
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread