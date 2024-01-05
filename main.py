import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b