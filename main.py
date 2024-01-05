numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)