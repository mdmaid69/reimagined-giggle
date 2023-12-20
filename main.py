  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def delete_file(file_name):
        os.remove(file_name)