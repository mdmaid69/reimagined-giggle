import time
def get_current_time():
        return time.ctime()
n = 10
print("Powers of 2:", [2**x for x in range(n)])