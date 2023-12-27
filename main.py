import re
def split_string(pattern, string):
        return re.split(pattern, string)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])