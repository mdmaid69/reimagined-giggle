  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))