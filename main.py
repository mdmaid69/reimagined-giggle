import random
print(random.randint(0, 100))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)