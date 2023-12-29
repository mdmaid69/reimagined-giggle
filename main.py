  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))