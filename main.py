import time
def get_current_time():
        return time.ctime()
n = 10
print("Square numbers:", [x**2 for x in range(n)])