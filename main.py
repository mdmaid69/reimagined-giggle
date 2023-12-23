import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def find_difference(list1, list2):
        return set(list1) - set(list2)