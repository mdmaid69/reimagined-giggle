import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])