import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])