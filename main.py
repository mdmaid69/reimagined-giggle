import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import datetime
def get_today_date():
        return datetime.date.today()