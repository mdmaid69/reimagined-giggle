import array
def convert_array_to_list(array):
        return array.tolist()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread