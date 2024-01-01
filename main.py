import re
print(re.match("h.*o", "hello world"))
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)