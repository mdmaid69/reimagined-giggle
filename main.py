import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())