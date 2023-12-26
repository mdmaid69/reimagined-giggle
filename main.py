import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def convert_array_to_bytes(array):
        return array.tobytes()