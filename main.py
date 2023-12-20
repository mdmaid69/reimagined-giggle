import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import datetime
def get_current_datetime():
        return datetime.datetime.now()