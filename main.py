import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1