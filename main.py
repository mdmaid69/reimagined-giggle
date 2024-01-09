def calculate_average(lst):
        return sum(lst) / len(lst)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())