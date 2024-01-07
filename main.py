  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))