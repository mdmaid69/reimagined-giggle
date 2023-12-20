  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))