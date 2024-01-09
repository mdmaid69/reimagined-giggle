import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def greet(name):
        print(f"Hello, {name}!")