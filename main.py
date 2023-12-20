import datetime
print(datetime.datetime.now())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)