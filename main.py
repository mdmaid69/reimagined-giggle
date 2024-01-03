import glob
def find_files(pattern):
        return glob.glob(pattern)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)