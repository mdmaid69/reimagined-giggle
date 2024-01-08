numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)