import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def convert_to_hex(n):
        return hex(n)