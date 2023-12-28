import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def calculate_perimeter_triangle(a, b, c):
        return a + b + c