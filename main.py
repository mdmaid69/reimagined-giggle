def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread