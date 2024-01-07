import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])