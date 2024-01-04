import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)