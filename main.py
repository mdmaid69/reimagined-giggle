import time
def get_current_time():
        return time.ctime()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])