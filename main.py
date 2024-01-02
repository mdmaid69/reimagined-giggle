import datetime
def get_current_datetime():
        return datetime.datetime.now()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a