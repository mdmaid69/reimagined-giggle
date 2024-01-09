import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)