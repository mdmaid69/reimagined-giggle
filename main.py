import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])