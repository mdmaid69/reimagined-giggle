import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread