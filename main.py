import array
def get_bytes_from_array(array):
        return array.tobytes()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())