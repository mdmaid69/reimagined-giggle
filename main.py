import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
x = 10
y = 20
print("Sum:", x + y)