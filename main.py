import re
def split_string(pattern, string):
        return re.split(pattern, string)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])