  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))