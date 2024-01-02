import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
name = "Python"
print("Hello,", name)