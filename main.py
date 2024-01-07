import re
print(re.match("h.*o", "hello world"))
import os
def get_file_size(filename):
        return os.path.getsize(filename)