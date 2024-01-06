import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)