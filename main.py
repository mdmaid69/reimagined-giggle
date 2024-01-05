import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))