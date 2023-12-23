import datetime
def get_today_date():
        return datetime.date.today()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a