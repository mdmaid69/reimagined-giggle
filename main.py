  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))