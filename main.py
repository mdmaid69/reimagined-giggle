def calculate_roi(gain, cost):
        return (gain - cost) / cost
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())