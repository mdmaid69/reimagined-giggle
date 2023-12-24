import re
print(re.match("h.*o", "hello world"))
import re
def split_string(pattern, string):
        return re.split(pattern, string)