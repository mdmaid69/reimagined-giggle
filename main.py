import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def find_max(lst):
        return max(lst)