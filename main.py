import time
def get_current_time():
        return time.ctime()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)