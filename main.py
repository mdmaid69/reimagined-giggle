import time
def get_time_since_epoch():
        return time.time()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])