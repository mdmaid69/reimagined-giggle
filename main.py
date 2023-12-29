import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread