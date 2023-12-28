from collections import Counter
print(Counter("hello world"))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)