  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))