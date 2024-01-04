import datetime
def get_today_date():
        return datetime.date.today()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)