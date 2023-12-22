import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)