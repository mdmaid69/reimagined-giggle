import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)