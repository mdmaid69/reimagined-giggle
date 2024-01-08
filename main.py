import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import shutil
def delete_directory(path):
        shutil.rmtree(path)