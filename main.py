import time
def get_current_time():
        return time.ctime()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)