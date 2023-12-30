import array
def convert_array_to_unicode(array):
        return array.tounicode()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread