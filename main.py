import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
n = 10
print("Powers of 2:", [2**x for x in range(n)])