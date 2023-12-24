import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread