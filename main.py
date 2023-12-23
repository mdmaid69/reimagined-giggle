import random
print(random.randint(0, 100))
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)