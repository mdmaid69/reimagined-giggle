sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)