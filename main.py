import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))