import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)