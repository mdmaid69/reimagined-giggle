import re
def split_string(pattern, string):
        return re.split(pattern, string)
def greet(name):
        print(f"Hello, {name}!")