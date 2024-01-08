import re
def split_string(pattern, string):
        return re.split(pattern, string)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])