import re
print(re.match("h.*o", "hello world"))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)