numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)