import re
def split_string(pattern, string):
        return re.split(pattern, string)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)