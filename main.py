import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread