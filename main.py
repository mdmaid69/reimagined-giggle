import array
def convert_array_to_unicode(array):
        return array.tounicode()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())