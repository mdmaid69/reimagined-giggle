import glob
def find_files(pattern):
        return glob.glob(pattern)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)