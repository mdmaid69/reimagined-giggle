import time
def get_current_time():
        return time.ctime()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])