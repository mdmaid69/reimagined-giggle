import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
i = 0
while i < 5:
        print(i)
        i += 1