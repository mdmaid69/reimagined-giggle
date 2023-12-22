import re
print(re.match("h.*o", "hello world"))
import glob
def find_files(pattern):
        return glob.glob(pattern)