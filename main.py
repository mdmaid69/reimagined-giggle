import array
def iterate_over_array(array):
        for item in array:
        print(item)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread