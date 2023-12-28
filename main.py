def find_min(lst):
        return min(lst)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread