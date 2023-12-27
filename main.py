import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def find_difference(list1, list2):
        return set(list1) - set(list2)