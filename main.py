import array
def iterate_over_array(array):
        for item in array:
        print(item)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())