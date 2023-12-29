import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_area_triangle(b, h):
        return 0.5 * b * h