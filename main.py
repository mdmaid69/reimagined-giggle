import datetime
print(datetime.datetime.now())
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)