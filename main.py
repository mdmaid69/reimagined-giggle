import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import re
print(re.match("h.*o", "hello world"))