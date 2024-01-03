import datetime
def get_current_date():
        return datetime.date.today()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable