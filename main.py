import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_area(radius):
        return 3.14 * radius * radius