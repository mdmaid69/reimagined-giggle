import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import datetime
def get_today_date():
        return datetime.date.today()