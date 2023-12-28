  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))