n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import re
def split_string(pattern, string):
        return re.split(pattern, string)