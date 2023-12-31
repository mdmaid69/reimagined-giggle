import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
i = 0
while i < 5:
        print(i)
        i += 1