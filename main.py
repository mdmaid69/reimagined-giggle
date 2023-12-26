import time
def get_current_time():
        return time.time()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b