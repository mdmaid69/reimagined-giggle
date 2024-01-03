import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def greet(name):
        print(f"Hello, {name}!")