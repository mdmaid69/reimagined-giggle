  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))