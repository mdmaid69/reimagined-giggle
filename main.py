import array
def get_array_item_count(array, item):
        return array.count(item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread