print([x**2 for x in range(10)])
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)