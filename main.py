def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())