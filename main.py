import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import glob
def find_files(pattern):
        return glob.glob(pattern)