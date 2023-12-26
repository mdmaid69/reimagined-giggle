import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import glob
def find_files(pattern):
        return glob.glob(pattern)