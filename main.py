import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def remove_duplicates(lst):
        return list(set(lst))