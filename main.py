import datetime
def get_current_date():
        return datetime.date.today()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))