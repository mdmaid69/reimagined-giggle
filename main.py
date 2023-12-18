import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)