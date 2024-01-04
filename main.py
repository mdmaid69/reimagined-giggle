import datetime
def get_current_datetime():
        return datetime.datetime.now()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))