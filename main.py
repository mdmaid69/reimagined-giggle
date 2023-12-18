import time
def get_current_time():
        return time.ctime()
def calculate_roi(gain, cost):
        return (gain - cost) / cost