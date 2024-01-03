import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def greet(name):
        print(f"Hello, {name}!")