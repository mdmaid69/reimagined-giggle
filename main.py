import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread