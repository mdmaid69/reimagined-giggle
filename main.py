import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])