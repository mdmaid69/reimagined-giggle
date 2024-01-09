n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)