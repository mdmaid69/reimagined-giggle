import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))