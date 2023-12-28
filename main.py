import datetime
def get_current_datetime():
        return datetime.datetime.now()
def find_difference(list1, list2):
        return set(list1) - set(list2)