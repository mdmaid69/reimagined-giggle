import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def greet(name):
        print(f"Hello, {name}!")