import re
def split_string(pattern, string):
        return re.split(pattern, string)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])