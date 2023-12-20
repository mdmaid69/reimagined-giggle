sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)