import glob
def find_files(pattern):
        return glob.glob(pattern)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)