import datetime
def get_current_datetime():
        return datetime.datetime.now()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}