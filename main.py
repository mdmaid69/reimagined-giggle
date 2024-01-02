import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])