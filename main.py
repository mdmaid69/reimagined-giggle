import datetime
def get_current_datetime():
        return datetime.datetime.now()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)